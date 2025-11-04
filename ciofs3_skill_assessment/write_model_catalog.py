import intake

# I don't think we need this since the models are built into PTM

cat = intake.entry.Catalog()

# Old CIOFS hindcast
dataset_id = "ciofs_hindcast"
url = "/home/kristen/projects/kerchunk_setup/ciofs_hindcast_kerchunk.parquet"
# url = "/media/data/kristen/kerchunk_setup/ciofs_hindcast_kerchunk.parquet"
# url = "/mnt/vault/ciofs/HINDCAST/ciofs_kerchunk.parq"
data = intake.readers.datatypes.HDF5(url)
initial_reader = data.to_reader("xarray:Dataset", engine="kerchunk", chunks={})
cat[dataset_id] = initial_reader
cat.aliases[dataset_id] = dataset_id

# New CIOFS freshwater
dataset_id = "ciofs_fresh"
# url = "/media/data/kristen/kerchunk_setup/ciofs_fresh_kerchunk.parquet"
# url = "/home/kristen/projects/kerchunk_setup/ciofs_fresh_kerchunk.parq"
url = "/home/kristen/projects/kerchunk_setup/ciofs_fresh_kerchunk.parquet"
data = intake.readers.datatypes.HDF5(url)
initial_reader = data.to_reader("xarray:Dataset", engine="kerchunk", chunks={})
cat[dataset_id] = initial_reader
cat.aliases[dataset_id] = dataset_id

# CIOFS3
dataset_id = "ciofs3"  # use this name regardless of version so results are in the same cache folder
url = "/home/kristen/projects/kerchunk_setup/ciofs3_v5_kerchunk.parquet"
data = intake.readers.datatypes.HDF5(url)
initial_reader = data.to_reader("xarray:Dataset", engine="kerchunk", chunks={})
cat[dataset_id] = initial_reader
cat.aliases[dataset_id] = dataset_id

# # CIOFS3
# dataset_id = "ciofs3"  # use this name regardless of version so results are in the same cache folder
# url = "/home/kristen/projects/kerchunk_setup/ciofs3_v4j_kerchunk.parquet"
# data = intake.readers.datatypes.HDF5(url)
# initial_reader = data.to_reader("xarray:Dataset", engine="kerchunk", chunks={})
# cat[dataset_id] = initial_reader
# cat.aliases[dataset_id] = dataset_id

# # CIOFS3
# dataset_id = "ciofs3"  # use this name regardless of version so results are in the same cache folder
# url = "/home/kristen/projects/kerchunk_setup/ciofs3_v4c_kerchunk.parquet"
# data = intake.readers.datatypes.HDF5(url)
# initial_reader = data.to_reader("xarray:Dataset", engine="kerchunk", chunks={})
# cat[dataset_id] = initial_reader
# cat.aliases[dataset_id] = dataset_id

# # CIOFS3
# dataset_id = "ciofs3"  # use this name regardless of version so results are in the same cache folder
# url = "/home/kristen/projects/kerchunk_setup/ciofs3_v4b_kerchunk.parquet"
# data = intake.readers.datatypes.HDF5(url)
# initial_reader = data.to_reader("xarray:Dataset", engine="kerchunk", chunks={})
# cat[dataset_id] = initial_reader
# cat.aliases[dataset_id] = dataset_id

# # CIOFS3
# dataset_id = "ciofs3"  # use this name regardless of version so results are in the same cache folder
# url = "/home/kristen/projects/kerchunk_setup/ciofs3_v4a_kerchunk.parquet"
# data = intake.readers.datatypes.HDF5(url)
# initial_reader = data.to_reader("xarray:Dataset", engine="kerchunk", chunks={})
# cat[dataset_id] = initial_reader
# cat.aliases[dataset_id] = dataset_id

# # CIOFS3
# dataset_id = "ciofs3"  # use this name regardless of version so results are in the same cache folder
# url = "/home/kristen/projects/kerchunk_setup/ciofs3_v4_kerchunk.parquet"
# data = intake.readers.datatypes.HDF5(url)
# initial_reader = data.to_reader("xarray:Dataset", engine="kerchunk", chunks={})
# cat[dataset_id] = initial_reader
# cat.aliases[dataset_id] = dataset_id

# # CIOFS3
# dataset_id = "ciofs3"  # use this name regardless of version so results are in the same cache folder
# url = "/home/kristen/projects/kerchunk_setup/ciofs3_v3_kerchunk.parquet"
# data = intake.readers.datatypes.HDF5(url)
# initial_reader = data.to_reader("xarray:Dataset", engine="kerchunk", chunks={})
# cat[dataset_id] = initial_reader
# cat.aliases[dataset_id] = dataset_id

# # CIOFS3
# dataset_id = "ciofs3"  # use this name regardless of version so results are in the same cache folder
# url = "/home/kristen/projects/kerchunk_setup/ciofs3_v2_kerchunk.parquet"
# data = intake.readers.datatypes.HDF5(url)
# initial_reader = data.to_reader("xarray:Dataset", engine="kerchunk", chunks={})
# cat[dataset_id] = initial_reader
# cat.aliases[dataset_id] = dataset_id

# # CIOFS3
# dataset_id = "ciofs3"  # use this name regardless of version so results are in the same cache folder
# url = "/home/kristen/projects/kerchunk_setup/ciofs3_v1_kerchunk.parquet"
# data = intake.readers.datatypes.HDF5(url)
# initial_reader = data.to_reader("xarray:Dataset", engine="kerchunk", chunks={})
# cat[dataset_id] = initial_reader
# cat.aliases[dataset_id] = dataset_id

cat.to_yaml_file("models.yaml")
import urllib.request
import json

urls = {
    "dashboard_raw.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzY0NjlhMzc1ZGFhNTQ2YTJhNGY0MTViYjA1OTIyNjYwEgsSBxCLh5zA1RQYAZIBJAoKcHJvamVjdF9pZBIWQhQxNjE4Mzk4MDcwOTE2OTY0NTA1MA&filename=&opi=89354086",
    "resources_raw.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sX2I3MzMyZmFmNWJkYjQ3NmNiNjhhOThjYjU4OTIzZGEyEgsSBxCLh5zA1RQYAZIBJAoKcHJvamVjdF9pZBIWQhQxNjE4Mzk4MDcwOTE2OTY0NTA1MA&filename=&opi=89354086",
    "simulation_raw.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sX2JhNGU3YzkzOTRjNjQ5MGI5NDI3ZWQ4YzVjYWU2OTcxEgsSBxCLh5zA1RQYAZIBJAoKcHJvamVjdF9pZBIWQhQxNjE4Mzk4MDcwOTE2OTY0NTA1MA&filename=&opi=89354086",
    "blockmap_raw.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sX2NkNGVlZWI0NjFlYTQyZTc5MGVjZDkyZmRhMzg3ZTNhEgsSBxCLh5zA1RQYAZIBJAoKcHJvamVjdF9pZBIWQhQxNjE4Mzk4MDcwOTE2OTY0NTA1MA&filename=&opi=89354086"
}

for name, url in urls.items():
    print(f"Downloading {name}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(name, 'wb') as out_file:
                out_file.write(response.read())
        print(f"Successfully downloaded {name}")
    except Exception as e:
        print(f"Error downloading {name}: {e}")

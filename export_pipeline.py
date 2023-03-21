from streamsets.sdk import ControlHub
import os
import time
from git import Repo
import git

CREDENTIAL_ID='12ce05ba-bc21-4ed5-9574-330de2949cae'
TOKEN='eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJzIjoiMmM4Y2NjMjczMmRhZjRjYTJjNDBlYTI0ZjZhN2RhYzMzY2QwMmMxZDYyZWZjZjRjNDIxZWY4ZGU2ODYxMmMyYWY5YjgxZGJjOGY1NmNiMzFjYTJkZjRjY2VjOGI2MTc5ZjMzNTE4NjMzODk1ZmFjNmNkZWVkMzcwNmM0ZDY4MzUiLCJ2IjoxLCJpc3MiOiJldTAxIiwianRpIjoiMTJjZTA1YmEtYmMyMS00ZWQ1LTk1NzQtMzMwZGUyOTQ5Y2FlIiwibyI6ImE2NzU2ZTM3LTZjYTktMTFlZC1hYWUwLTJmNWFmZWRhYzJlOCJ9.'
sch = ControlHub(CREDENTIAL_ID, TOKEN)

def Export(pipeline_name, version,path):
    try:
        print("inside export")
        sch_pipeline = sch.pipelines.get(name=pipeline_name)
        commit_id = ""
        for pipeline in sch_pipeline.commits:
            if pipeline.version == version:
                commit_id = pipeline.commit_id
        sch_pipeline = sch.pipelines.get(commit_id=commit_id)
        print(sch_pipeline)
        lst = []
        lst.append(sch_pipeline)

        pipeline_zip_data = sch.export_pipelines(lst)
        # print(pipeline_zip_data)

        # Write to an archive the exported pipeline
        with open(path, 'wb') as pipelines_zip_file:
            pipelines_zip_file.write(pipeline_zip_data)
    except Exception as e:
        print(e)

# import pdb
# pdb.set_trace()
def Import(path):
    print("inside import")
    try:
        with open(path, 'rb') as input_file:
            pipelines_imported = sch.import_pipelines_from_archive(input_file, 'Import Pipeline using SDK')
    except Exception as e:
        print(e)

def check_in_check_out():
    # git.Git("D:/test1").clone("https://github.com/sudshinde/test")
    repo = git.Repo('D:/test/test')
    repo.git.add('--all')
    repo.git.commit('-m', 'commit second file')
    print("himanshu 5")
    origin = repo.remote(name='origin')
    print("himanshu 10")
    origin.push()
    print("himanshu 15")
    # repo.remote().fetch()

check_in_check_out()

Export("jdbc connection pieline","1","D:/tmp/sample_imported_pipeline.zip")
# Import("D:/tmp/sample_imported_pipeline.zip")

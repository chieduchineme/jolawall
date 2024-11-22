import re
import re
from collections import defaultdict

def extract_last_versions_to_file(log_lines, output_file):
    """
    Extracts the last package versions from the 'Downloading' log lines and writes them into a Python file.
    The version is extracted up to the last integer before an alphabet is met.
    Only the last version seen in the log is kept for each package.
    
    Args:
        log_lines (list of str): The list of log lines.
        output_file (str): The path of the Python file to write the result to.
    """
    package_dict = {}
    
    for line in log_lines:
        if "Downloading" in line:
            # Extract the package name and version number using regex
            match = re.search(r"Downloading ([\w\-\_]+)-([\d\.]+)", line)
            if match:
                package_name = match.group(1)
                version = match.group(2)
                # Update the dictionary to only keep the last version for each package
                package_dict[package_name] = version
    
    # Prepare the list of package strings
    package_list = [f"{name}=={version}" for name, version in package_dict.items()]
    
    # Write to the Python file
    with open(output_file, 'w') as f:
        f.write("# Generated list of latest package versions\n")
        f.write("packages = [\n")
        for package in package_list:
            f.write(f"    '{package}',\n")
        f.write("]\n")

# Example usage with your provided data:
log_data = """
#6 DONE 0.5s
#5 [1/5] FROM docker.io/library/python:3.11.4-slim@sha256:17d62d681d9ecef20aae6c6605e9cf83b0ba3dc247013e2f43e1b5a045ad4901
#5 sha256:52d2b7f179e32b4cbd579ee3c4958027988f9a8274850ab0c7c24661e3adaac5 29.12MB / 29.12MB 0.4s done
#5 sha256:46233543d8c2dc599bdb9d522180ca9e14cad4ac2017a5dc481660bfa4aa3ed9 3.38MB / 3.38MB 0.4s done
#5 extracting sha256:52d2b7f179e32b4cbd579ee3c4958027988f9a8274850ab0c7c24661e3adaac5 1.0s done
#5 extracting sha256:2b8a9a2240c1224b34f6aafbc3310f9a3fe65bd6893050906d02e89fc8326aa9
#5 extracting sha256:2b8a9a2240c1224b34f6aafbc3310f9a3fe65bd6893050906d02e89fc8326aa9 0.1s done
#5 extracting sha256:051d6521462a7eb4ca0374e97701d6eec68eb51b118d3ef5d002798b498fb12e
#5 extracting sha256:051d6521462a7eb4ca0374e97701d6eec68eb51b118d3ef5d002798b498fb12e 0.9s done
#5 extracting sha256:fce84b1f897c621e9474bd4d5a49e2e22fa35e248e78e754010d34ec3d2d28cd
#5 extracting sha256:fce84b1f897c621e9474bd4d5a49e2e22fa35e248e78e754010d34ec3d2d28cd done
#5 extracting sha256:46233543d8c2dc599bdb9d522180ca9e14cad4ac2017a5dc481660bfa4aa3ed9 0.1s
#5 extracting sha256:46233543d8c2dc599bdb9d522180ca9e14cad4ac2017a5dc481660bfa4aa3ed9 0.2s done
#5 DONE 3.1s
#7 [2/5] WORKDIR /AiGuard
#7 DONE 0.0s
#8 [3/5] COPY requirements.txt .
#8 DONE 0.0s
#9 [4/5] RUN pip install --no-cache-dir -r requirements.txt
#9 1.597 Collecting arrow==1.3.0 (from -r requirements.txt (line 1))
#9 1.634   Downloading arrow-1.3.0-py3-none-any.whl (66 kB)
#9 1.648      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.4/66.4 kB 4.9 MB/s eta 0:00:00
#9 1.675 Collecting asgiref==3.8.1 (from -r requirements.txt (line 2))
#9 1.678   Downloading asgiref-3.8.1-py3-none-any.whl (23 kB)
#9 1.743 Collecting astroid==3.3.5 (from -r requirements.txt (line 3))
#9 1.748   Downloading astroid-3.3.5-py3-none-any.whl (274 kB)
#9 1.755      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 274.6/274.6 kB 52.3 MB/s eta 0:00:00
#9 1.773 Collecting asttokens==2.4.1 (from -r requirements.txt (line 4))
#9 1.776   Downloading asttokens-2.4.1-py2.py3-none-any.whl (27 kB)
#9 1.789 Collecting astunparse==1.6.3 (from -r requirements.txt (line 5))
#9 1.792   Downloading astunparse-1.6.3-py2.py3-none-any.whl (12 kB)
#9 1.811 Collecting beautifulsoup4==4.12.3 (from -r requirements.txt (line 6))
#9 1.814   Downloading beautifulsoup4-4.12.3-py3-none-any.whl (147 kB)
#9 1.817      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 147.9/147.9 kB 220.5 MB/s eta 0:00:00
#9 1.839 Collecting bitsandbytes==0.44.1 (from -r requirements.txt (line 7))
#9 1.843   Downloading bitsandbytes-0.44.1-py3-none-manylinux_2_24_x86_64.whl (122.4 MB)
#9 2.419      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 122.4/122.4 MB 254.9 MB/s eta 0:00:00
#9 2.561 Collecting bleach==6.1.0 (from -r requirements.txt (line 8))
#9 2.566   Downloading bleach-6.1.0-py3-none-any.whl (162 kB)
#9 2.568      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 162.8/162.8 kB 266.3 MB/s eta 0:00:00
#9 3.059 Collecting boto3==1.35.5 (from -r requirements.txt (line 9))
#9 3.067   Downloading boto3-1.35.5-py3-none-any.whl (139 kB)
#9 3.070      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 139.1/139.1 kB 239.5 MB/s eta 0:00:00
#9 3.606 Collecting botocore==1.35.5 (from -r requirements.txt (line 10))
#9 3.610   Downloading botocore-1.35.5-py3-none-any.whl (12.5 MB)
#9 3.666      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.5/12.5 MB 243.6 MB/s eta 0:00:00
#9 3.730 Collecting cachetools==5.5.0 (from -r requirements.txt (line 11))
#9 3.734   Downloading cachetools-5.5.0-py3-none-any.whl (9.5 kB)
#9 3.760 Collecting colorama==0.4.6 (from -r requirements.txt (line 12))
#9 3.764   Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
#9 3.797 Collecting datasets==3.0.1 (from -r requirements.txt (line 13))
#9 3.801   Downloading datasets-3.0.1-py3-none-any.whl (471 kB)
#9 3.804      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 471.6/471.6 kB 286.9 MB/s eta 0:00:00
#9 3.975 Collecting debugpy==1.8.0 (from -r requirements.txt (line 14))
#9 3.979   Downloading debugpy-1.8.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
#9 3.996      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 222.6 MB/s eta 0:00:00
#9 4.019 Collecting decorator==5.1.1 (from -r requirements.txt (line 15))
#9 4.022   Downloading decorator-5.1.1-py3-none-any.whl (9.1 kB)
#9 4.120 Collecting Django==3.0 (from -r requirements.txt (line 16))
#9 4.124   Downloading Django-3.0-py3-none-any.whl (7.4 MB)
#9 4.169      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.4/7.4 MB 181.1 MB/s eta 0:00:00
#9 4.383 Collecting django-admin (from -r requirements.txt (line 17))
#9 4.387   Downloading django_admin-2.0.2-py2.py3-none-any.whl (7.6 kB)
#9 4.413 Collecting django-cors-headers (from -r requirements.txt (line 18))
#9 4.417   Downloading django_cors_headers-4.6.0-py3-none-any.whl (12 kB)
#9 4.496 Collecting django-excel-response2 (from -r requirements.txt (line 19))
#9 4.500   Downloading django_excel_response2-3.0.6-py2.py3-none-any.whl (4.9 kB)
#9 4.535 Collecting django-extensions (from -r requirements.txt (line 20))
#9 4.539   Downloading django_extensions-3.2.3-py3-none-any.whl (229 kB)
#9 4.541      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.9/229.9 kB 277.9 MB/s eta 0:00:00
#9 4.618 Collecting django-grpc==1.0.21 (from -r requirements.txt (line 21))
#9 4.623   Downloading django_grpc-1.0.21-py2.py3-none-any.whl (14 kB)
#9 4.695 Collecting django-six (from -r requirements.txt (line 22))
#9 4.833   Downloading django_six-1.0.5-py2.py3-none-any.whl (2.7 kB)
#9 4.909 Collecting djangogrpcframework==0.2.1 (from -r requirements.txt (line 23))
#9 4.913   Downloading djangogrpcframework-0.2.1-py2.py3-none-any.whl (20 kB)
#9 4.949 Collecting djangorestframework (from -r requirements.txt (line 24))
#9 4.955   Downloading djangorestframework-3.15.2-py3-none-any.whl (1.1 MB)
#9 4.961      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 239.0 MB/s eta 0:00:00
#9 4.981 Collecting docopt==0.6.2 (from -r requirements.txt (line 25))
#9 4.983   Downloading docopt-0.6.2.tar.gz (25 kB)
#9 4.991   Preparing metadata (setup.py): started
#9 5.426   Preparing metadata (setup.py): finished with status 'done'
#9 5.503 Collecting excel-base==1.0.4 (from -r requirements.txt (line 26))
#9 5.507   Downloading excel_base-1.0.4-py2.py3-none-any.whl (5.2 kB)
#9 5.521 Collecting executing==2.0.1 (from -r requirements.txt (line 27))
#9 5.524   Downloading executing-2.0.1-py2.py3-none-any.whl (24 kB)
#9 5.580 Collecting faiss-cpu==1.8.0.post1 (from -r requirements.txt (line 28))
#9 5.585   Downloading faiss_cpu-1.8.0.post1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (27.0 MB)
#9 5.702      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 27.0/27.0 MB 282.9 MB/s eta 0:00:00
#9 5.862 Collecting Faker==30.8.2 (from -r requirements.txt (line 29))
#9 5.866   Downloading Faker-30.8.2-py3-none-any.whl (1.8 MB)
#9 5.875      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 277.5 MB/s eta 0:00:00
#9 6.169 Collecting fastavro==1.9.5 (from -r requirements.txt (line 30))
#9 6.174   Downloading fastavro-1.9.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.3 MB)
#9 6.190      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 229.3 MB/s eta 0:00:00
#9 6.210 Collecting fastjsonschema==2.19.1 (from -r requirements.txt (line 31))
#9 6.213   Downloading fastjsonschema-2.19.1-py3-none-any.whl (23 kB)
#9 6.240 Collecting filelock==3.13.1 (from -r requirements.txt (line 32))
#9 6.244   Downloading filelock-3.13.1-py3-none-any.whl (11 kB)
#9 6.259 Collecting flatbuffers==24.3.25 (from -r requirements.txt (line 33))
#9 6.261   Downloading flatbuffers-24.3.25-py2.py3-none-any.whl (26 kB)
#9 6.444 Collecting fonttools==4.47.2 (from -r requirements.txt (line 34))
#9 6.448   Downloading fonttools-4.47.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.9 MB)
#9 6.468      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.9/4.9 MB 279.6 MB/s eta 0:00:00
#9 6.490 Collecting fqdn==1.5.1 (from -r requirements.txt (line 35))
#9 6.493   Downloading fqdn-1.5.1-py3-none-any.whl (9.1 kB)
#9 6.585 Collecting frozenlist==1.4.1 (from -r requirements.txt (line 36))
#9 6.589   Downloading frozenlist-1.4.1-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (272 kB)
#9 6.592      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 272.3/272.3 kB 286.8 MB/s eta 0:00:00
#9 6.624 Collecting fsspec==2023.12.2 (from -r requirements.txt (line 37))
#9 6.628   Downloading fsspec-2023.12.2-py3-none-any.whl (168 kB)
#9 6.630      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 169.0/169.0 kB 272.1 MB/s eta 0:00:00
#9 6.646 Collecting gast==0.4.0 (from -r requirements.txt (line 38))
#9 6.649   Downloading gast-0.4.0-py3-none-any.whl (9.8 kB)
#9 6.727 Collecting gensim==4.3.3 (from -r requirements.txt (line 39))
#9 6.731   Downloading gensim-4.3.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (26.7 MB)
#9 6.906      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 26.7/26.7 MB 198.9 MB/s eta 0:00:00
#9 7.937 Collecting grpcio (from -r requirements.txt (line 40))
#9 7.940   Downloading grpcio-1.68.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (5.9 MB)
#9 7.965      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.9/5.9 MB 283.6 MB/s eta 0:00:00
#9 8.991 Collecting grpcio-tools (from -r requirements.txt (line 41))
#9 8.996   Downloading grpcio_tools-1.68.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.4 MB)
#9 9.008      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.4/2.4 MB 238.8 MB/s eta 0:00:00
#9 9.033 Collecting gunicorn==23.0.0 (from -r requirements.txt (line 42))
#9 9.036   Downloading gunicorn-23.0.0-py3-none-any.whl (85 kB)
#9 9.038      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 85.0/85.0 kB 250.1 MB/s eta 0:00:00
#9 9.107 Collecting h5py==3.10.0 (from -r requirements.txt (line 43))
#9 9.112   Downloading h5py-3.10.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.8 MB)
#9 9.142      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.8/4.8 MB 174.0 MB/s eta 0:00:00
#9 9.175 Collecting httpcore==1.0.5 (from -r requirements.txt (line 44))
#9 9.178   Downloading httpcore-1.0.5-py3-none-any.whl (77 kB)
#9 9.180      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 77.9/77.9 kB 250.9 MB/s eta 0:00:00
#9 9.199 Collecting httplib2==0.22.0 (from -r requirements.txt (line 45))
#9 9.202   Downloading httplib2-0.22.0-py3-none-any.whl (96 kB)
#9 9.205      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.9/96.9 kB 256.0 MB/s eta 0:00:00
#9 9.234 Collecting httpx==0.27.0 (from -r requirements.txt (line 46))
#9 9.241   Downloading httpx-0.27.0-py3-none-any.whl (75 kB)
#9 9.243      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 75.6/75.6 kB 211.6 MB/s eta 0:00:00
#9 9.256 Collecting httpx-sse==0.4.0 (from -r requirements.txt (line 47))
#9 9.259   Downloading httpx_sse-0.4.0-py3-none-any.whl (7.8 kB)
#9 9.310 Collecting huggingface-hub==0.24.6 (from -r requirements.txt (line 48))
#9 9.315   Downloading huggingface_hub-0.24.6-py3-none-any.whl (417 kB)
#9 9.318      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 417.5/417.5 kB 283.8 MB/s eta 0:00:00
#9 9.337 Collecting idna==3.8 (from -r requirements.txt (line 49))
#9 9.340   Downloading idna-3.8-py3-none-any.whl (66 kB)
#9 9.342      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.9/66.9 kB 187.1 MB/s eta 0:00:00
#9 9.380 Collecting imageio==2.36.0 (from -r requirements.txt (line 50))
#9 9.384   Downloading imageio-2.36.0-py3-none-any.whl (315 kB)
#9 9.388      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 315.4/315.4 kB 211.9 MB/s eta 0:00:00
#9 9.406 Collecting immutabledict==4.2.1 (from -r requirements.txt (line 51))
#9 9.410   Downloading immutabledict-4.2.1-py3-none-any.whl (4.7 kB)
#9 9.422 Collecting importlab==0.8.1 (from -r requirements.txt (line 52))
#9 9.426   Downloading importlab-0.8.1-py2.py3-none-any.whl (21 kB)
#9 9.438 Collecting imutils==0.5.4 (from -r requirements.txt (line 53))
#9 9.442   Downloading imutils-0.5.4.tar.gz (17 kB)
#9 9.449   Preparing metadata (setup.py): started
#9 9.639   Preparing metadata (setup.py): finished with status 'done'
#9 9.693 Collecting ipykernel==6.29.0 (from -r requirements.txt (line 54))
#9 9.698   Downloading ipykernel-6.29.0-py3-none-any.whl (116 kB)
#9 9.700      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 116.1/116.1 kB 262.1 MB/s eta 0:00:00
#9 9.761 Collecting ipython==8.12.3 (from -r requirements.txt (line 55))
#9 9.766   Downloading ipython-8.12.3-py3-none-any.whl (798 kB)
#9 9.771      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 798.3/798.3 kB 277.9 MB/s eta 0:00:00
#9 9.785 Collecting ipython-genutils==0.2.0 (from -r requirements.txt (line 56))
#9 9.788   Downloading ipython_genutils-0.2.0-py2.py3-none-any.whl (26 kB)
#9 9.830 Collecting ipywidgets==8.1.5 (from -r requirements.txt (line 57))
#9 9.835   Downloading ipywidgets-8.1.5-py3-none-any.whl (139 kB)
#9 9.838      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 139.8/139.8 kB 246.3 MB/s eta 0:00:00
#9 9.849 Collecting isoduration==20.11.0 (from -r requirements.txt (line 58))
#9 9.852   Downloading isoduration-20.11.0-py3-none-any.whl (11 kB)
#9 9.901 Collecting isort==5.13.2 (from -r requirements.txt (line 59))
#9 9.905   Downloading isort-5.13.2-py3-none-any.whl (92 kB)
#9 9.907      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 92.3/92.3 kB 222.9 MB/s eta 0:00:00
#9 9.987 Collecting isoweek==1.3.3 (from -r requirements.txt (line 60))
#9 9.992   Downloading isoweek-1.3.3-py2.py3-none-any.whl (7.1 kB)
#9 10.01 Collecting jedi==0.19.1 (from -r requirements.txt (line 61))
#9 10.02   Downloading jedi-0.19.1-py2.py3-none-any.whl (1.6 MB)
#9 10.03      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 283.5 MB/s eta 0:00:00
#9 10.06 Collecting Jinja2==3.1.3 (from -r requirements.txt (line 62))
#9 10.06   Downloading Jinja2-3.1.3-py3-none-any.whl (133 kB)
#9 10.07      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.2/133.2 kB 262.2 MB/s eta 0:00:00
#9 10.08 Collecting jmespath==1.0.1 (from -r requirements.txt (line 63))
#9 10.08   Downloading jmespath-1.0.1-py3-none-any.whl (20 kB)
#9 10.11 Collecting joblib==1.3.2 (from -r requirements.txt (line 64))
#9 10.11   Downloading joblib-1.3.2-py3-none-any.whl (302 kB)
#9 10.11      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 302.2/302.2 kB 280.7 MB/s eta 0:00:00
#9 10.14 Collecting json5==0.9.25 (from -r requirements.txt (line 65))
#9 10.14   Downloading json5-0.9.25-py3-none-any.whl (30 kB)
#9 10.16 Collecting jsonpointer==3.0.0 (from -r requirements.txt (line 66))
#9 10.16   Downloading jsonpointer-3.0.0-py2.py3-none-any.whl (7.6 kB)
#9 10.19 Collecting jsonschema==4.23.0 (from -r requirements.txt (line 67))
#9 10.20   Downloading jsonschema-4.23.0-py3-none-any.whl (88 kB)
#9 10.20      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 88.5/88.5 kB 250.4 MB/s eta 0:00:00
#9 10.22 Collecting jsonschema-specifications==2023.12.1 (from -r requirements.txt (line 68))
#9 10.22   Downloading jsonschema_specifications-2023.12.1-py3-none-any.whl (18 kB)
#9 10.25 Collecting keras==2.13.1 (from -r requirements.txt (line 69))
#9 10.25   Downloading keras-2.13.1-py3-none-any.whl (1.7 MB)
#9 10.26      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 277.2 MB/s eta 0:00:00
#9 10.36 Collecting kiwisolver==1.4.5 (from -r requirements.txt (line 70))
#9 10.37   Downloading kiwisolver-1.4.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.4 MB)
#9 10.38      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 282.1 MB/s eta 0:00:00
#9 10.39 Collecting lazy_loader==0.4 (from -r requirements.txt (line 71))
#9 10.39   Downloading lazy_loader-0.4-py3-none-any.whl (12 kB)
#9 10.42 Collecting libclang==18.1.1 (from -r requirements.txt (line 72))
#9 10.42   Downloading libclang-18.1.1-py2.py3-none-manylinux2010_x86_64.whl (24.5 MB)
#9 10.51      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 24.5/24.5 MB 277.3 MB/s eta 0:00:00
#9 10.62 Collecting libcst==1.5.1 (from -r requirements.txt (line 73))
#9 10.63   Downloading libcst-1.5.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.3 MB)
#9 10.64      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 291.2 MB/s eta 0:00:00
#9 10.74 Collecting llvmlite==0.43.0 (from -r requirements.txt (line 74))
#9 10.75   Downloading llvmlite-0.43.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (43.9 MB)
#9 10.95      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.9/43.9 MB 261.3 MB/s eta 0:00:00
#9 11.01 Collecting Markdown==3.7 (from -r requirements.txt (line 75))
#9 11.01   Downloading Markdown-3.7-py3-none-any.whl (106 kB)
#9 11.02      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 106.3/106.3 kB 258.2 MB/s eta 0:00:00
#9 11.14 Collecting markdown-it-py==3.0.0 (from -r requirements.txt (line 76))
#9 11.14   Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
#9 11.15      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 87.5/87.5 kB 240.4 MB/s eta 0:00:00
#9 11.24 Collecting MarkupSafe==2.1.3 (from -r requirements.txt (line 77))
#9 11.25   Downloading MarkupSafe-2.1.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (28 kB)
#9 11.48 Collecting matplotlib==3.8.2 (from -r requirements.txt (line 78))
#9 11.48   Downloading matplotlib-3.8.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.6 MB)
#9 11.54      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.6/11.6 MB 232.4 MB/s eta 0:00:00
#9 11.56 Collecting matplotlib-inline==0.1.6 (from -r requirements.txt (line 79))
#9 11.57   Downloading matplotlib_inline-0.1.6-py3-none-any.whl (9.4 kB)
#9 11.58 Collecting mccabe==0.7.0 (from -r requirements.txt (line 80))
#9 11.58   Downloading mccabe-0.7.0-py2.py3-none-any.whl (7.3 kB)
#9 11.59 Collecting mdurl==0.1.2 (from -r requirements.txt (line 81))
#9 11.60   Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
#9 11.62 Collecting mistune==3.0.2 (from -r requirements.txt (line 82))
#9 11.62   Downloading mistune-3.0.2-py3-none-any.whl (47 kB)
#9 11.62      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 48.0/48.0 kB 218.3 MB/s eta 0:00:00
#9 11.66 Collecting ml-dtypes (from -r requirements.txt (line 83))
#9 11.67   Downloading ml_dtypes-0.5.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.5 MB)
#9 11.73      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 68.0 MB/s eta 0:00:00
#9 11.75 Collecting mpmath==1.3.0 (from -r requirements.txt (line 84))
#9 11.76   Downloading mpmath-1.3.0-py3-none-any.whl (536 kB)
#9 11.76      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.2/536.2 kB 250.0 MB/s eta 0:00:00
#9 11.87 Collecting msgspec==0.18.6 (from -r requirements.txt (line 85))
#9 11.87   Downloading msgspec-0.18.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (209 kB)
#9 11.87      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 209.5/209.5 kB 272.6 MB/s eta 0:00:00
#9 12.17 Collecting multidict==6.1.0 (from -r requirements.txt (line 86))
#9 12.17   Downloading multidict-6.1.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (129 kB)
#9 12.18      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 129.0/129.0 kB 262.8 MB/s eta 0:00:00
#9 12.21 Collecting multiprocess==0.70.16 (from -r requirements.txt (line 87))
#9 12.21   Downloading multiprocess-0.70.16-py311-none-any.whl (143 kB)
#9 12.21      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 143.5/143.5 kB 259.6 MB/s eta 0:00:00
#9 12.24 Collecting nbformat==5.10.4 (from -r requirements.txt (line 88))
#9 12.24   Downloading nbformat-5.10.4-py3-none-any.whl (78 kB)
#9 12.24      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.5/78.5 kB 237.2 MB/s eta 0:00:00
#9 12.27 Collecting nest-asyncio==1.5.9 (from -r requirements.txt (line 89))
#9 12.27   Downloading nest_asyncio-1.5.9-py3-none-any.whl (5.3 kB)
#9 12.30 Collecting networkx==3.2.1 (from -r requirements.txt (line 90))
#9 12.31   Downloading networkx-3.2.1-py3-none-any.whl (1.6 MB)
#9 12.32      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 248.8 MB/s eta 0:00:00
#9 12.37 Collecting ninja==1.11.1.1 (from -r requirements.txt (line 91))
#9 12.37   Downloading ninja-1.11.1.1-py2.py3-none-manylinux1_x86_64.manylinux_2_5_x86_64.whl (307 kB)
#9 12.38      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 307.2/307.2 kB 275.7 MB/s eta 0:00:00
#9 12.55 Collecting numba (from -r requirements.txt (line 92))
#9 12.55   Downloading numba-0.60.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (3.7 MB)
#9 12.56      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.7/3.7 MB 282.9 MB/s eta 0:00:00
#9 12.88 Collecting numpy (from -r requirements.txt (line 93))
#9 12.89   Downloading numpy-2.1.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.3 MB)
#9 12.96      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.3/16.3 MB 249.6 MB/s eta 0:00:00
#9 13.01 Collecting packaging==23.2 (from -r requirements.txt (line 94))
#9 13.01   Downloading packaging-23.2-py3-none-any.whl (53 kB)
#9 13.01      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 53.0/53.0 kB 231.4 MB/s eta 0:00:00
#9 13.32 Collecting pandas==2.2.0 (from -r requirements.txt (line 95))
#9 13.33   Downloading pandas-2.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (13.0 MB)
#9 13.38      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.0/13.0 MB 251.4 MB/s eta 0:00:00
#9 13.42 Collecting pandocfilters==1.5.1 (from -r requirements.txt (line 96))
#9 13.42   Downloading pandocfilters-1.5.1-py2.py3-none-any.whl (8.7 kB)
#9 13.44 Collecting parso==0.8.3 (from -r requirements.txt (line 97))
#9 13.44   Downloading parso-0.8.3-py2.py3-none-any.whl (100 kB)
#9 13.44      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.8/100.8 kB 252.1 MB/s eta 0:00:00
#9 13.73 Collecting pillow==10.3.0 (from -r requirements.txt (line 98))
#9 13.74   Downloading pillow-10.3.0-cp311-cp311-manylinux_2_28_x86_64.whl (4.5 MB)
#9 13.75      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 284.5 MB/s eta 0:00:00
#9 13.84 Collecting pipreqs==0.5.0 (from -r requirements.txt (line 99))
#9 13.85   Downloading pipreqs-0.5.0-py3-none-any.whl (33 kB)
#9 13.87 Collecting platformdirs==4.1.0 (from -r requirements.txt (line 100))
#9 13.88   Downloading platformdirs-4.1.0-py3-none-any.whl (17 kB)
#9 13.89 Collecting ply==3.11 (from -r requirements.txt (line 101))
#9 13.89   Downloading ply-3.11-py2.py3-none-any.whl (49 kB)
#9 13.89      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 49.6/49.6 kB 194.8 MB/s eta 0:00:00
#9 13.91 Collecting prometheus_client==0.20.0 (from -r requirements.txt (line 102))
#9 13.91   Downloading prometheus_client-0.20.0-py3-none-any.whl (54 kB)
#9 13.92      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 54.5/54.5 kB 208.9 MB/s eta 0:00:00
#9 13.96 Collecting prompt-toolkit==3.0.43 (from -r requirements.txt (line 103))
#9 13.96   Downloading prompt_toolkit-3.0.43-py3-none-any.whl (386 kB)
#9 13.97      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 386.1/386.1 kB 273.3 MB/s eta 0:00:00
#9 13.99 Collecting proto-plus (from -r requirements.txt (line 104))
#9 14.00   Downloading proto_plus-1.25.0-py3-none-any.whl (50 kB)
#9 14.00      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 50.1/50.1 kB 178.2 MB/s eta 0:00:00
#9 14.29 Collecting protobuf==5.28.3 (from -r requirements.txt (line 105))
#9 14.29   Downloading protobuf-5.28.3-cp38-abi3-manylinux2014_x86_64.whl (316 kB)
#9 14.30      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 316.6/316.6 kB 280.7 MB/s eta 0:00:00
#9 14.42 Collecting psutil==5.9.8 (from -r requirements.txt (line 106))
#9 14.42   Downloading psutil-5.9.8-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (288 kB)
#9 14.43      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 288.2/288.2 kB 257.8 MB/s eta 0:00:00
#9 14.44 Collecting pure-eval==0.2.2 (from -r requirements.txt (line 107))
#9 14.45   Downloading pure_eval-0.2.2-py3-none-any.whl (11 kB)
#9 14.46 Collecting py-cpuinfo==9.0.0 (from -r requirements.txt (line 108))
#9 14.46   Downloading py_cpuinfo-9.0.0-py3-none-any.whl (22 kB)
#9 14.60 Collecting pyarrow==17.0.0 (from -r requirements.txt (line 109))
#9 14.60   Downloading pyarrow-17.0.0-cp311-cp311-manylinux_2_28_x86_64.whl (39.9 MB)
#9 14.75      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 39.9/39.9 MB 281.9 MB/s eta 0:00:00
#9 14.81 Collecting pyasn1==0.6.0 (from -r requirements.txt (line 110))
#9 14.82   Downloading pyasn1-0.6.0-py2.py3-none-any.whl (85 kB)
#9 14.82      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 85.3/85.3 kB 253.6 MB/s eta 0:00:00
#9 14.84 Collecting pyasn1_modules==0.4.0 (from -r requirements.txt (line 111))
#9 14.85   Downloading pyasn1_modules-0.4.0-py3-none-any.whl (181 kB)
#9 14.85      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 181.2/181.2 kB 233.9 MB/s eta 0:00:00
#9 14.87 Collecting pycnite==2024.7.31 (from -r requirements.txt (line 112))
#9 14.87   Downloading pycnite-2024.7.31-py3-none-any.whl (22 kB)
#9 14.88 Collecting pycparser==2.22 (from -r requirements.txt (line 113))
#9 14.89   Downloading pycparser-2.22-py3-none-any.whl (117 kB)
#9 14.89      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 117.6/117.6 kB 259.5 MB/s eta 0:00:00
#9 15.09 Collecting pydantic==2.8.2 (from -r requirements.txt (line 114))
#9 15.09   Downloading pydantic-2.8.2-py3-none-any.whl (423 kB)
#9 15.10      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 423.9/423.9 kB 290.0 MB/s eta 0:00:00
#9 16.34 Collecting pydantic_core==2.20.1 (from -r requirements.txt (line 115))
#9 16.35   Downloading pydantic_core-2.20.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
#9 16.36      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 257.9 MB/s eta 0:00:00
#9 16.37 Collecting pydot==3.0.2 (from -r requirements.txt (line 116))
#9 16.38   Downloading pydot-3.0.2-py3-none-any.whl (35 kB)
#9 16.40 Collecting Pygments==2.17.2 (from -r requirements.txt (line 117))
#9 16.41   Downloading pygments-2.17.2-py3-none-any.whl (1.2 MB)
#9 16.41      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 251.7 MB/s eta 0:00:00
#9 16.48 Collecting pylint==3.3.1 (from -r requirements.txt (line 118))
#9 16.50   Downloading pylint-3.3.1-py3-none-any.whl (521 kB)
#9 16.50      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 521.8/521.8 kB 258.3 MB/s eta 0:00:00
#9 16.52 Collecting pynndescent==0.5.13 (from -r requirements.txt (line 119))
#9 16.52   Downloading pynndescent-0.5.13-py3-none-any.whl (56 kB)
#9 16.52      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 56.9/56.9 kB 230.7 MB/s eta 0:00:00
#9 16.56 Collecting pyparsing==3.1.4 (from -r requirements.txt (line 120))
#9 16.56   Downloading pyparsing-3.1.4-py3-none-any.whl (104 kB)
#9 16.56      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 104.1/104.1 kB 249.9 MB/s eta 0:00:00
#9 16.58 Collecting python-dateutil==2.8.2 (from -r requirements.txt (line 121))
#9 16.59   Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
#9 16.59      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 247.7/247.7 kB 283.2 MB/s eta 0:00:00
#9 16.61 Collecting python-dotenv==1.0.1 (from -r requirements.txt (line 122))
#9 16.61   Downloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)
#9 16.63 Collecting python-json-logger==2.0.7 (from -r requirements.txt (line 123))
#9 16.63   Downloading python_json_logger-2.0.7-py3-none-any.whl (8.1 kB)
#9 16.70 Collecting python-mnist==0.7 (from -r requirements.txt (line 124))
#9 16.71   Downloading python_mnist-0.7-py2.py3-none-any.whl (9.6 kB)
#9 16.89 Collecting pytype==2024.10.11 (from -r requirements.txt (line 125))
#9 16.89   Downloading pytype-2024.10.11-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (4.7 MB)
#9 16.94      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.7/4.7 MB 114.2 MB/s eta 0:00:00
#9 17.02 Collecting pytz==2023.3.post1 (from -r requirements.txt (line 126))
#9 17.02   Downloading pytz-2023.3.post1-py2.py3-none-any.whl (502 kB)
#9 17.02      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 502.5/502.5 kB 281.4 MB/s eta 0:00:00
#9 17.09 Collecting PyYAML==6.0.2 (from -r requirements.txt (line 127))
#9 17.09   Downloading PyYAML-6.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (762 kB)
#9 17.10      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 763.0/763.0 kB 264.6 MB/s eta 0:00:00
#9 17.52 Collecting pyzmq==25.1.2 (from -r requirements.txt (line 128))
#9 17.53   Downloading pyzmq-25.1.2-cp311-cp311-manylinux_2_28_x86_64.whl (1.1 MB)
#9 17.54      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 166.3 MB/s eta 0:00:00
#9 17.57 Collecting qtconsole==5.5.2 (from -r requirements.txt (line 129))
#9 17.57   Downloading qtconsole-5.5.2-py3-none-any.whl (123 kB)
#9 17.57      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 123.4/123.4 kB 243.7 MB/s eta 0:00:00
#9 17.60 Collecting QtPy==2.4.1 (from -r requirements.txt (line 130))
#9 17.60   Downloading QtPy-2.4.1-py3-none-any.whl (93 kB)
#9 17.60      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 93.5/93.5 kB 239.9 MB/s eta 0:00:00
#9 17.64 Collecting referencing==0.35.1 (from -r requirements.txt (line 131))
#9 17.65   Downloading referencing-0.35.1-py3-none-any.whl (26 kB)
#9 18.29 Collecting regex==2024.7.24 (from -r requirements.txt (line 132))
#9 18.29   Downloading regex-2024.7.24-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (786 kB)
#9 18.30      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 786.6/786.6 kB 260.8 MB/s eta 0:00:00
#9 18.50 Collecting requests==2.32.3 (from -r requirements.txt (line 133))
#9 18.51   Downloading requests-2.32.3-py3-none-any.whl (64 kB)
#9 18.51      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.9/64.9 kB 234.2 MB/s eta 0:00:00
#9 18.52 Collecting requests-oauthlib==1.3.1 (from -r requirements.txt (line 134))
#9 18.53   Downloading requests_oauthlib-1.3.1-py2.py3-none-any.whl (23 kB)
#9 18.54 Collecting rfc3339-validator==0.1.4 (from -r requirements.txt (line 135))
#9 18.54   Downloading rfc3339_validator-0.1.4-py2.py3-none-any.whl (3.5 kB)
#9 18.56 Collecting rfc3986-validator==0.1.1 (from -r requirements.txt (line 136))
#9 18.56   Downloading rfc3986_validator-0.1.1-py2.py3-none-any.whl (4.2 kB)
#9 18.97 Collecting rpds-py==0.20.0 (from -r requirements.txt (line 137))
#9 18.97   Downloading rpds_py-0.20.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (354 kB)
#9 18.98      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 354.8/354.8 kB 274.7 MB/s eta 0:00:00
#9 18.99 Collecting rsa==4.9 (from -r requirements.txt (line 138))
#9 19.00   Downloading rsa-4.9-py3-none-any.whl (34 kB)
#9 19.03 Collecting s3transfer==0.10.2 (from -r requirements.txt (line 139))
#9 19.03   Downloading s3transfer-0.10.2-py3-none-any.whl (82 kB)
#9 19.03      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 82.7/82.7 kB 242.5 MB/s eta 0:00:00
#9 19.25 Collecting safetensors==0.4.5 (from -r requirements.txt (line 140))
#9 19.26   Downloading safetensors-0.4.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (435 kB)
#9 19.26      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 435.0/435.0 kB 283.8 MB/s eta 0:00:00
#9 19.28 Collecting scapy==2.6.0 (from -r requirements.txt (line 141))
#9 19.28   Downloading scapy-2.6.0-py3-none-any.whl (2.4 MB)
#9 19.30      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.4/2.4 MB 198.6 MB/s eta 0:00:00
#9 19.45 Collecting scikit-learn==1.4.0 (from -r requirements.txt (line 142))
#9 19.45   Downloading scikit_learn-1.4.0-1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.1 MB)
#9 19.51      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.1/12.1 MB 247.1 MB/s eta 0:00:00
#9 19.71 Collecting scipy==1.12.0 (from -r requirements.txt (line 143))
#9 19.71   Downloading scipy-1.12.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (38.4 MB)
#9 19.87      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 38.4/38.4 MB 242.8 MB/s eta 0:00:00
#9 19.99 Collecting screen==1.0.1 (from -r requirements.txt (line 144))
#9 20.18   Downloading screen-1.0.1.tar.gz (8.6 kB)
#9 20.19   Preparing metadata (setup.py): started
#9 20.39   Preparing metadata (setup.py): finished with status 'done'
#9 20.41 Collecting seaborn==0.13.1 (from -r requirements.txt (line 145))
#9 20.41   Downloading seaborn-0.13.1-py3-none-any.whl (294 kB)
#9 20.42      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 294.8/294.8 kB 241.7 MB/s eta 0:00:00
#9 20.43 Collecting Send2Trash==1.8.3 (from -r requirements.txt (line 146))
#9 20.43   Downloading Send2Trash-1.8.3-py3-none-any.whl (18 kB)
#9 20.48 Collecting setuptools-scm==8.0.4 (from -r requirements.txt (line 147))
#9 20.48   Downloading setuptools_scm-8.0.4-py3-none-any.whl (42 kB)
#9 20.49      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.1/42.1 kB 196.8 MB/s eta 0:00:00
#9 21.22 Collecting simsimd==6.0.7 (from -r requirements.txt (line 148))
#9 21.23   Downloading simsimd-6.0.7-cp311-cp311-manylinux_2_28_x86_64.whl (606 kB)
#9 21.23      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 606.4/606.4 kB 201.4 MB/s eta 0:00:00
#9 21.25 Collecting six==1.16.0 (from -r requirements.txt (line 149))
#9 21.25   Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
#9 21.28 Collecting smart-open==7.0.5 (from -r requirements.txt (line 150))
#9 21.28   Downloading smart_open-7.0.5-py3-none-any.whl (61 kB)
#9 21.28      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.4/61.4 kB 240.7 MB/s eta 0:00:00
#9 21.29 Collecting sniffio==1.3.1 (from -r requirements.txt (line 151))
#9 21.29   Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
#9 21.32 Collecting soupsieve==2.6 (from -r requirements.txt (line 152))
#9 21.32   Downloading soupsieve-2.6-py3-none-any.whl (36 kB)
#9 21.33 Collecting tabulate==0.9.0 (from -r requirements.txt (line 153))
#9 21.34   Downloading tabulate-0.9.0-py3-none-any.whl (35 kB)
#9 21.37 Collecting tensorboard (from -r requirements.txt (line 154))
#9 21.37   Downloading tensorboard-2.18.0-py3-none-any.whl (5.5 MB)
#9 21.41      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 133.7 MB/s eta 0:00:00
#9 21.44 Collecting tensorboard-data-server==0.7.2 (from -r requirements.txt (line 155))
#9 21.44   Downloading tensorboard_data_server-0.7.2-py3-none-manylinux_2_31_x86_64.whl (6.6 MB)
#9 21.46      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.6/6.6 MB 294.6 MB/s eta 0:00:00
#9 21.66 Collecting tensorflow (from -r requirements.txt (line 156))
#9 21.66   Downloading tensorflow-2.18.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (615.4 MB)
#9 23.97      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 615.4/615.4 MB 281.2 MB/s eta 0:00:00
#9 24.65 Collecting tensorflow-estimator==2.15.0 (from -r requirements.txt (line 157))
#9 24.65   Downloading tensorflow_estimator-2.15.0-py2.py3-none-any.whl (441 kB)
#9 24.66      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 442.0/442.0 kB 279.1 MB/s eta 0:00:00
#9 24.71 Collecting tensorflow-io-gcs-filesystem==0.31.0 (from -r requirements.txt (line 158))
#9 24.71   Downloading tensorflow_io_gcs_filesystem-0.31.0-cp311-cp311-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (2.4 MB)
#9 24.79      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.4/2.4 MB 32.1 MB/s eta 0:00:00
#9 24.80 Collecting termcolor==2.4.0 (from -r requirements.txt (line 159))
#9 24.81   Downloading termcolor-2.4.0-py3-none-any.whl (7.7 kB)
#9 24.83 Collecting terminado==0.18.1 (from -r requirements.txt (line 160))
#9 24.83   Downloading terminado-0.18.1-py3-none-any.whl (14 kB)
#9 24.84 Collecting threadpoolctl==3.2.0 (from -r requirements.txt (line 161))
#9 24.85   Downloading threadpoolctl-3.2.0-py3-none-any.whl (15 kB)
#9 24.87 Collecting thriftpy2==0.5.2 (from -r requirements.txt (line 162))
#9 24.87   Downloading thriftpy2-0.5.2.tar.gz (782 kB)
#9 24.88      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 782.3/782.3 kB 227.5 MB/s eta 0:00:00
#9 24.96   Installing build dependencies: started
#9 27.57   Installing build dependencies: finished with status 'done'
#9 27.57   Getting requirements to build wheel: started
#9 29.09   Getting requirements to build wheel: finished with status 'done'
#9 29.09   Preparing metadata (pyproject.toml): started
#9 29.60   Preparing metadata (pyproject.toml): finished with status 'done'
#9 29.65 Collecting tifffile==2024.9.20 (from -r requirements.txt (line 163))
#9 29.66   Downloading tifffile-2024.9.20-py3-none-any.whl (228 kB)
#9 29.66      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 228.2/228.2 kB 243.7 MB/s eta 0:00:00
#9 29.76 Collecting TimeConvert==3.0.13 (from -r requirements.txt (line 164))
#9 29.76   Downloading TimeConvert-3.0.13-py2.py3-none-any.whl (19 kB)
#9 30.28 Collecting tokenizers==0.13.3 (from -r requirements.txt (line 165))
#9 30.29   Downloading tokenizers-0.13.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (7.8 MB)
#9 30.32      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.8/7.8 MB 237.6 MB/s eta 0:00:00
#9 30.34 Collecting toml==0.10.2 (from -r requirements.txt (line 166))
#9 30.35   Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)
#9 30.38 Collecting tomlkit==0.13.2 (from -r requirements.txt (line 167))
#9 30.38   Downloading tomlkit-0.13.2-py3-none-any.whl (37 kB)
#9 30.46 Collecting torch==2.1.2 (from -r requirements.txt (line 168))
#9 30.46   Downloading torch-2.1.2-cp311-cp311-manylinux1_x86_64.whl (670.2 MB)
#9 34.19      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 670.2/670.2 MB 205.0 MB/s eta 0:00:00
#9 34.95 Collecting torchvision==0.16.2 (from -r requirements.txt (line 169))
#9 34.96   Downloading torchvision-0.16.2-cp311-cp311-manylinux1_x86_64.whl (6.8 MB)
#9 35.00      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.8/6.8 MB 157.0 MB/s eta 0:00:00
#9 35.07 Collecting transformers==4.31.0 (from -r requirements.txt (line 170))
#9 35.08   Downloading transformers-4.31.0-py3-none-any.whl (7.4 MB)
#9 35.14      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.4/7.4 MB 133.9 MB/s eta 0:00:00
#9 35.19 Collecting types-requests==2.32.0.20240712 (from -r requirements.txt (line 171))
#9 35.19   Downloading types_requests-2.32.0.20240712-py3-none-any.whl (15 kB)
#9 35.21 Collecting typing_extensions==4.12.2 (from -r requirements.txt (line 172))
#9 35.22   Downloading typing_extensions-4.12.2-py3-none-any.whl (37 kB)
#9 35.23 Collecting webencodings==0.5.1 (from -r requirements.txt (line 173))
#9 35.23   Downloading webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
#9 35.26 Collecting websocket-client==1.7.0 (from -r requirements.txt (line 174))
#9 35.27   Downloading websocket_client-1.7.0-py3-none-any.whl (58 kB)
#9 35.27      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.5/58.5 kB 229.1 MB/s eta 0:00:00
#9 35.31 Collecting types-python-dateutil>=2.8.10 (from arrow==1.3.0->-r requirements.txt (line 1))
#9 35.31   Downloading types_python_dateutil-2.9.0.20241003-py3-none-any.whl (9.7 kB)
#9 35.33 Requirement already satisfied: wheel<1.0,>=0.23.0 in /usr/local/lib/python3.11/site-packages (from astunparse==1.6.3->-r requirements.txt (line 5)) (0.41.1)
#9 35.51 Collecting urllib3!=2.2.0,<3,>=1.25.4 (from botocore==1.35.5->-r requirements.txt (line 10))
#9 35.51   Downloading urllib3-2.2.3-py3-none-any.whl (126 kB)
#9 35.52      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 126.3/126.3 kB 264.8 MB/s eta 0:00:00
#9 35.64 Collecting dill<0.3.9,>=0.3.0 (from datasets==3.0.1->-r requirements.txt (line 13))
#9 35.64   Downloading dill-0.3.8-py3-none-any.whl (116 kB)
#9 35.65      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 116.3/116.3 kB 268.7 MB/s eta 0:00:00
#9 35.71 Collecting tqdm>=4.66.3 (from datasets==3.0.1->-r requirements.txt (line 13))
#9 35.71   Downloading tqdm-4.67.0-py3-none-any.whl (78 kB)
#9 35.72      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.6/78.6 kB 232.2 MB/s eta 0:00:00
#9 35.86 Collecting xxhash (from datasets==3.0.1->-r requirements.txt (line 13))
#9 35.87   Downloading xxhash-3.5.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (194 kB)
#9 35.87      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 194.8/194.8 kB 272.3 MB/s eta 0:00:00
#9 35.88 Collecting fsspec[http]<=2024.6.1,>=2023.1.0 (from datasets==3.0.1->-r requirements.txt (line 13))
#9 35.89   Downloading fsspec-2024.6.1-py3-none-any.whl (177 kB)
#9 35.89      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 177.6/177.6 kB 252.1 MB/s eta 0:00:00
#9 36.60 Collecting aiohttp (from datasets==3.0.1->-r requirements.txt (line 13))
#9 36.61   Downloading aiohttp-3.11.7-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.7 MB)
#9 36.61      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 250.3 MB/s eta 0:00:00
#9 36.66 Collecting sqlparse>=0.2.2 (from Django==3.0->-r requirements.txt (line 16))
#9 36.66   Downloading sqlparse-0.5.2-py3-none-any.whl (44 kB)
#9 36.66      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.4/44.4 kB 179.9 MB/s eta 0:00:00
#9 36.67 Requirement already satisfied: setuptools in /usr/local/lib/python3.11/site-packages (from django-grpc==1.0.21->-r requirements.txt (line 21)) (65.5.1)
#9 36.69 Collecting xlwt (from excel-base==1.0.4->-r requirements.txt (line 26))
#9 36.70   Downloading xlwt-1.3.0-py2.py3-none-any.whl (99 kB)
#9 36.70      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.0/100.0 kB 250.2 MB/s eta 0:00:00
#9 36.73 Collecting numpy (from -r requirements.txt (line 93))
#9 36.73   Downloading numpy-1.26.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (18.3 MB)
#9 36.82      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.3/18.3 MB 220.0 MB/s eta 0:00:00
#9 37.06 Collecting certifi (from httpcore==1.0.5->-r requirements.txt (line 44))
#9 37.07   Downloading certifi-2024.8.30-py3-none-any.whl (167 kB)
#9 37.07      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 167.3/167.3 kB 209.4 MB/s eta 0:00:00
#9 37.08 Collecting h11<0.15,>=0.13 (from httpcore==1.0.5->-r requirements.txt (line 44))
#9 37.08   Downloading h11-0.14.0-py3-none-any.whl (58 kB)
#9 37.09      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.3/58.3 kB 215.6 MB/s eta 0:00:00
#9 37.15 Collecting anyio (from httpx==0.27.0->-r requirements.txt (line 46))
#9 37.15   Downloading anyio-4.6.2.post1-py3-none-any.whl (90 kB)
#9 37.16      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 90.4/90.4 kB 258.7 MB/s eta 0:00:00
#9 37.37 Collecting comm>=0.1.1 (from ipykernel==6.29.0->-r requirements.txt (line 54))
#9 37.37   Downloading comm-0.2.2-py3-none-any.whl (7.2 kB)
#9 37.43 Collecting jupyter-client>=6.1.12 (from ipykernel==6.29.0->-r requirements.txt (line 54))
#9 37.44   Downloading jupyter_client-8.6.3-py3-none-any.whl (106 kB)
#9 37.44      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 106.1/106.1 kB 262.5 MB/s eta 0:00:00
#9 37.47 Collecting jupyter-core!=5.0.*,>=4.12 (from ipykernel==6.29.0->-r requirements.txt (line 54))
#9 37.48   Downloading jupyter_core-5.7.2-py3-none-any.whl (28 kB)
#9 37.55 Collecting tornado>=6.1 (from ipykernel==6.29.0->-r requirements.txt (line 54))
#9 37.55   Downloading tornado-6.4.2-cp38-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (437 kB)
#9 37.55      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 437.2/437.2 kB 279.8 MB/s eta 0:00:00
#9 37.58 Collecting traitlets>=5.4.0 (from ipykernel==6.29.0->-r requirements.txt (line 54))
#9 37.58   Downloading traitlets-5.14.3-py3-none-any.whl (85 kB)
#9 37.59      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 85.4/85.4 kB 250.9 MB/s eta 0:00:00
#9 37.65 Collecting backcall (from ipython==8.12.3->-r requirements.txt (line 55))
#9 37.65   Downloading backcall-0.2.0-py2.py3-none-any.whl (11 kB)
#9 37.66 Collecting pickleshare (from ipython==8.12.3->-r requirements.txt (line 55))
#9 37.67   Downloading pickleshare-0.7.5-py2.py3-none-any.whl (6.9 kB)
#9 37.70 Collecting stack-data (from ipython==8.12.3->-r requirements.txt (line 55))
#9 37.86   Downloading stack_data-0.6.3-py3-none-any.whl (24 kB)
#9 37.88 Collecting pexpect>4.3 (from ipython==8.12.3->-r requirements.txt (line 55))
#9 37.88   Downloading pexpect-4.9.0-py2.py3-none-any.whl (63 kB)
#9 37.89      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.8/63.8 kB 252.3 MB/s eta 0:00:00
#9 37.96 Collecting widgetsnbextension~=4.0.12 (from ipywidgets==8.1.5->-r requirements.txt (line 57))
#9 37.97   Downloading widgetsnbextension-4.0.13-py3-none-any.whl (2.3 MB)
#9 37.98      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 235.0 MB/s eta 0:00:00
#9 38.02 Collecting jupyterlab-widgets~=3.0.12 (from ipywidgets==8.1.5->-r requirements.txt (line 57))
#9 38.02   Downloading jupyterlab_widgets-3.0.13-py3-none-any.whl (214 kB)
#9 38.03      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 214.4/214.4 kB 277.9 MB/s eta 0:00:00
#9 38.17 Collecting attrs>=22.2.0 (from jsonschema==4.23.0->-r requirements.txt (line 67))
#9 38.17   Downloading attrs-24.2.0-py3-none-any.whl (63 kB)
#9 38.18      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.0/63.0 kB 198.8 MB/s eta 0:00:00
#9 38.46 Collecting contourpy>=1.0.1 (from matplotlib==3.8.2->-r requirements.txt (line 78))
#9 38.47   Downloading contourpy-1.3.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (326 kB)
#9 38.47      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 326.2/326.2 kB 281.5 MB/s eta 0:00:00
#9 38.48 Collecting cycler>=0.10 (from matplotlib==3.8.2->-r requirements.txt (line 78))
#9 38.49   Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
#9 38.83 Collecting tzdata>=2022.7 (from pandas==2.2.0->-r requirements.txt (line 95))
#9 38.83   Downloading tzdata-2024.2-py2.py3-none-any.whl (346 kB)
#9 38.84      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 346.6/346.6 kB 197.2 MB/s eta 0:00:00
#9 38.94 Collecting nbconvert<8.0.0,>=7.11.0 (from pipreqs==0.5.0->-r requirements.txt (line 99))
#9 38.95   Downloading nbconvert-7.16.4-py3-none-any.whl (257 kB)
#9 38.95      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 257.4/257.4 kB 268.8 MB/s eta 0:00:00
#9 38.96 Collecting yarg==0.1.9 (from pipreqs==0.5.0->-r requirements.txt (line 99))
#9 38.97   Downloading yarg-0.1.9-py2.py3-none-any.whl (19 kB)
#9 39.04 Collecting wcwidth (from prompt-toolkit==3.0.43->-r requirements.txt (line 103))
#9 39.04   Downloading wcwidth-0.2.13-py2.py3-none-any.whl (34 kB)
#9 39.24 Collecting annotated-types>=0.4.0 (from pydantic==2.8.2->-r requirements.txt (line 114))
#9 39.25   Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
#9 39.82 Collecting charset-normalizer<4,>=2 (from requests==2.32.3->-r requirements.txt (line 133))
#9 39.83   Downloading charset_normalizer-3.4.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (142 kB)
#9 39.83      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 142.6/142.6 kB 271.2 MB/s eta 0:00:00
#9 39.88 Collecting oauthlib>=3.0.0 (from requests-oauthlib==1.3.1->-r requirements.txt (line 134))
#9 39.89   Downloading oauthlib-3.2.2-py3-none-any.whl (151 kB)
#9 39.89      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 151.7/151.7 kB 255.5 MB/s eta 0:00:00
#9 40.66 Collecting wrapt (from smart-open==7.0.5->-r requirements.txt (line 150))
#9 40.66   Downloading wrapt-1.17.0-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (83 kB)
#9 40.66      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 83.2/83.2 kB 240.1 MB/s eta 0:00:00
#9 40.85 Collecting ptyprocess (from terminado==0.18.1->-r requirements.txt (line 160))
#9 40.86   Downloading ptyprocess-0.7.0-py2.py3-none-any.whl (13 kB)
#9 41.55 Collecting Cython>=3.0.10 (from thriftpy2==0.5.2->-r requirements.txt (line 162))
#9 41.56   Downloading Cython-3.0.11-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.6 MB)
#9 41.62      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.6/3.6 MB 59.4 MB/s eta 0:00:00
#9 41.72 Collecting tzlocal (from TimeConvert==3.0.13->-r requirements.txt (line 164))
#9 41.72   Downloading tzlocal-5.2-py3-none-any.whl (17 kB)
#9 41.86 Collecting sympy (from torch==2.1.2->-r requirements.txt (line 168))
#9 41.86   Downloading sympy-1.13.3-py3-none-any.whl (6.2 MB)
#9 41.89      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.2/6.2 MB 263.4 MB/s eta 0:00:00
#9 41.92 Collecting nvidia-cuda-nvrtc-cu12==12.1.105 (from torch==2.1.2->-r requirements.txt (line 168))
#9 41.92   Downloading nvidia_cuda_nvrtc_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (23.7 MB)
#9 42.01      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 23.7/23.7 MB 275.9 MB/s eta 0:00:00
#9 42.05 Collecting nvidia-cuda-runtime-cu12==12.1.105 (from torch==2.1.2->-r requirements.txt (line 168))
#9 42.06   Downloading nvidia_cuda_runtime_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (823 kB)
#9 42.06      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 823.6/823.6 kB 278.0 MB/s eta 0:00:00
#9 42.08 Collecting nvidia-cuda-cupti-cu12==12.1.105 (from torch==2.1.2->-r requirements.txt (line 168))
#9 42.09   Downloading nvidia_cuda_cupti_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (14.1 MB)
#9 42.14      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.1/14.1 MB 277.8 MB/s eta 0:00:00
#9 42.23 Collecting nvidia-cudnn-cu12==8.9.2.26 (from torch==2.1.2->-r requirements.txt (line 168))
#9 42.23   Downloading nvidia_cudnn_cu12-8.9.2.26-py3-none-manylinux1_x86_64.whl (731.7 MB)
#9 45.81      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 731.7/731.7 MB 284.1 MB/s eta 0:00:00
#9 46.52 Collecting nvidia-cublas-cu12==12.1.3.1 (from torch==2.1.2->-r requirements.txt (line 168))
#9 46.53   Downloading nvidia_cublas_cu12-12.1.3.1-py3-none-manylinux1_x86_64.whl (410.6 MB)
#9 48.24      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 410.6/410.6 MB 291.0 MB/s eta 0:00:00
#9 48.64 Collecting nvidia-cufft-cu12==11.0.2.54 (from torch==2.1.2->-r requirements.txt (line 168))
#9 48.65   Downloading nvidia_cufft_cu12-11.0.2.54-py3-none-manylinux1_x86_64.whl (121.6 MB)
#9 49.10      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 121.6/121.6 MB 288.8 MB/s eta 0:00:00
#9 49.23 Collecting nvidia-curand-cu12==10.3.2.106 (from torch==2.1.2->-r requirements.txt (line 168))
#9 49.24   Downloading nvidia_curand_cu12-10.3.2.106-py3-none-manylinux1_x86_64.whl (56.5 MB)
#9 49.51      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 56.5/56.5 MB 240.7 MB/s eta 0:00:00
#9 49.58 Collecting nvidia-cusolver-cu12==11.4.5.107 (from torch==2.1.2->-r requirements.txt (line 168))
#9 49.58   Downloading nvidia_cusolver_cu12-11.4.5.107-py3-none-manylinux1_x86_64.whl (124.2 MB)
#9 50.26      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 124.2/124.2 MB 214.6 MB/s eta 0:00:00
#9 50.39 Collecting nvidia-cusparse-cu12==12.1.0.106 (from torch==2.1.2->-r requirements.txt (line 168))
#9 50.40   Downloading nvidia_cusparse_cu12-12.1.0.106-py3-none-manylinux1_x86_64.whl (196.0 MB)
#9 51.30      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 196.0/196.0 MB 244.1 MB/s eta 0:00:00
#9 51.50 Collecting nvidia-nccl-cu12==2.18.1 (from torch==2.1.2->-r requirements.txt (line 168))
#9 51.50   Downloading nvidia_nccl_cu12-2.18.1-py3-none-manylinux1_x86_64.whl (209.8 MB)
#9 52.43      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 209.8/209.8 MB 242.0 MB/s eta 0:00:00
#9 52.70 Collecting nvidia-nvtx-cu12==12.1.105 (from torch==2.1.2->-r requirements.txt (line 168))
#9 52.71   Downloading nvidia_nvtx_cu12-12.1.105-py3-none-manylinux1_x86_64.whl (99 kB)
#9 52.71      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 99.1/99.1 kB 204.4 MB/s eta 0:00:00
#9 52.73 Collecting triton==2.1.0 (from torch==2.1.2->-r requirements.txt (line 168))
#9 52.73   Downloading triton-2.1.0-0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (89.2 MB)
#9 53.22      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 89.2/89.2 MB 241.2 MB/s eta 0:00:00
#9 53.95 Collecting nvidia-nvjitlink-cu12 (from nvidia-cusolver-cu12==11.4.5.107->torch==2.1.2->-r requirements.txt (line 168))
#9 53.95   Downloading nvidia_nvjitlink_cu12-12.6.85-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl (19.7 MB)
#9 54.05      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 19.7/19.7 MB 234.7 MB/s eta 0:00:00
#9 54.26 INFO: pip is looking at multiple versions of django-cors-headers to determine which version is compatible with other requirements. This could take a while.
#9 54.26 Collecting django-cors-headers (from -r requirements.txt (line 18))
#9 54.26   Downloading django_cors_headers-4.5.0-py3-none-any.whl (12 kB)
#9 54.29   Downloading django_cors_headers-4.4.0-py3-none-any.whl (12 kB)
#9 54.30   Downloading django_cors_headers-4.3.1-py3-none-any.whl (12 kB)
#9 54.31   Downloading django_cors_headers-4.3.0-py3-none-any.whl (12 kB)
#9 54.33   Downloading django_cors_headers-4.2.0-py3-none-any.whl (12 kB)
#9 54.34   Downloading django_cors_headers-4.1.0-py3-none-any.whl (12 kB)
#9 54.35   Downloading django_cors_headers-4.0.0-py3-none-any.whl (12 kB)
#9 54.35 INFO: pip is looking at multiple versions of django-cors-headers to determine which version is compatible with other requirements. This could take a while.
#9 54.36   Downloading django_cors_headers-3.14.0-py3-none-any.whl (13 kB)
#9 54.37   Downloading django_cors_headers-3.13.0-py3-none-any.whl (13 kB)
#9 54.38   Downloading django_cors_headers-3.12.0-py3-none-any.whl (13 kB)
#9 54.39   Downloading django_cors_headers-3.11.0-py3-none-any.whl (12 kB)
#9 54.48 INFO: pip is looking at multiple versions of django-extensions to determine which version is compatible with other requirements. This could take a while.
#9 54.48 Collecting django-extensions (from -r requirements.txt (line 20))
#9 54.49   Downloading django_extensions-3.2.1-py3-none-any.whl (229 kB)
#9 54.49      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.4/229.4 kB 260.5 MB/s eta 0:00:00
#9 54.50   Downloading django_extensions-3.2.0-py3-none-any.whl (229 kB)
#9 54.51      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.1/229.1 kB 287.1 MB/s eta 0:00:00
#9 54.52   Downloading django_extensions-3.1.5-py3-none-any.whl (224 kB)
#9 54.52      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 224.2/224.2 kB 278.5 MB/s eta 0:00:00
#9 54.59 INFO: pip is looking at multiple versions of djangorestframework to determine which version is compatible with other requirements. This could take a while.
#9 54.59 Collecting djangorestframework (from -r requirements.txt (line 24))
#9 54.60   Downloading djangorestframework-3.15.1-py3-none-any.whl (1.1 MB)
#9 54.60      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 282.1 MB/s eta 0:00:00
#9 54.92 Collecting absl-py>=0.4 (from tensorboard->-r requirements.txt (line 154))
#9 54.92   Downloading absl_py-2.1.0-py3-none-any.whl (133 kB)
#9 54.92      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.7/133.7 kB 261.1 MB/s eta 0:00:00
#9 55.00 Collecting werkzeug>=1.0.1 (from tensorboard->-r requirements.txt (line 154))
#9 55.00   Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)
#9 55.00      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 224.5/224.5 kB 288.3 MB/s eta 0:00:00
#9 55.07 Collecting google-pasta>=0.1.1 (from tensorflow->-r requirements.txt (line 156))
#9 55.08   Downloading google_pasta-0.2.0-py3-none-any.whl (57 kB)
#9 55.08      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 57.5/57.5 kB 231.0 MB/s eta 0:00:00
#9 55.09 Collecting opt-einsum>=2.3.2 (from tensorflow->-r requirements.txt (line 156))
#9 55.10   Downloading opt_einsum-3.4.0-py3-none-any.whl (71 kB)
#9 55.10      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 71.9/71.9 kB 234.7 MB/s eta 0:00:00
#9 55.14 INFO: pip is looking at multiple versions of tensorflow to determine which version is compatible with other requirements. This could take a while.
#9 55.15 Collecting tensorflow (from -r requirements.txt (line 156))
#9 55.16   Downloading tensorflow-2.17.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (601.3 MB)
#9 59.62      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 601.3/601.3 MB 205.2 MB/s eta 0:00:00
#9 60.32 Collecting ml-dtypes (from -r requirements.txt (line 83))
#9 60.33   Downloading ml_dtypes-0.4.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.2 MB)
#9 60.34      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 296.8 MB/s eta 0:00:00
#9 60.36 Collecting tensorflow (from -r requirements.txt (line 156))
#9 60.37   Downloading tensorflow-2.17.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (601.3 MB)
#9 63.89      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 601.3/601.3 MB 178.4 MB/s eta 0:00:00
#9 64.60   Downloading tensorflow-2.16.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (590.7 MB)
#9 69.39      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 590.7/590.7 MB 228.7 MB/s eta 0:00:00
#9 70.09 Collecting ml-dtypes (from -r requirements.txt (line 83))
#9 70.09   Downloading ml_dtypes-0.3.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.2 MB)
#9 70.10      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 217.2 MB/s eta 0:00:00
#9 70.11 Collecting tensorflow (from -r requirements.txt (line 156))
#9 70.12   Downloading tensorflow-2.16.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (589.8 MB)
#9 74.68      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 589.8/589.8 MB 269.5 MB/s eta 0:00:00
#9 75.37   Downloading tensorflow-2.15.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (475.3 MB)
#9 81.15      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 475.3/475.3 MB 50.7 MB/s eta 0:00:00
#9 81.71   Downloading tensorflow-2.15.0.post1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (475.3 MB)
#9 84.60      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 475.3/475.3 MB 239.5 MB/s eta 0:00:00
#9 85.14 Collecting ml-dtypes (from -r requirements.txt (line 83))
#9 85.15   Downloading ml_dtypes-0.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.0 MB)
#9 85.15      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB 217.6 MB/s eta 0:00:00
#9 85.16 Collecting tensorflow (from -r requirements.txt (line 156))
#9 85.23   Downloading tensorflow-2.15.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (475.3 MB)
#9 91.34      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 475.3/475.3 MB 93.7 MB/s eta 0:00:00
#9 91.87 INFO: pip is looking at multiple versions of tensorflow to determine which version is compatible with other requirements. This could take a while.
#9 91.88   Downloading tensorflow-2.14.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (489.9 MB)
#9 94.81      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 489.9/489.9 MB 208.1 MB/s eta 0:00:00
#9 95.36   Downloading tensorflow-2.14.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (489.9 MB)
#9 100.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 489.9/489.9 MB 216.3 MB/s eta 0:00:00
#9 101.0   Downloading tensorflow-2.13.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (479.7 MB)
#9 105.3      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 479.7/479.7 MB 211.4 MB/s eta 0:00:00
#9 105.9 Collecting numpy (from -r requirements.txt (line 93))
#9 105.9   Downloading numpy-1.24.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (17.3 MB)
#9 105.9      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 17.3/17.3 MB 290.0 MB/s eta 0:00:00
#9 106.0 Collecting tensorflow (from -r requirements.txt (line 156))
#9 106.0   Downloading tensorflow-2.13.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (524.2 MB)
#9 110.9      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 524.2/524.2 MB 237.3 MB/s eta 0:00:00
#9 111.5   Downloading tensorflow-2.12.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (585.9 MB)
#9 118.9      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 585.9/585.9 MB 232.6 MB/s eta 0:00:00
#9 119.6 Collecting jax>=0.3.15 (from tensorflow->-r requirements.txt (line 156))
#9 119.6   Downloading jax-0.4.35-py3-none-any.whl (2.2 MB)
#9 119.6      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 289.1 MB/s eta 0:00:00
#9 119.6 INFO: This is taking longer than usual. You might need to provide the dependency resolver with stricter constraints to reduce runtime. See https://pip.pypa.io/warnings/backtracking for guidance. If you want to abort this run, press Ctrl + C.
#9 119.6 Collecting tensorflow (from -r requirements.txt (line 156))
#9 119.6   Downloading tensorflow-2.12.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (586.0 MB)
#9 124.3      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 586.0/586.0 MB 214.2 MB/s eta 0:00:00
#9 124.9 Collecting tensorboard (from -r requirements.txt (line 154))
#9 124.9   Downloading tensorboard-2.17.1-py3-none-any.whl (5.5 MB)
#9 125.0      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 192.8 MB/s eta 0:00:00
#9 125.3   Downloading tensorboard-2.17.0-py3-none-any.whl (5.5 MB)
#9 125.3      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 221.2 MB/s eta 0:00:00
#9 125.3 INFO: pip is looking at multiple versions of tensorboard to determine which version is compatible with other requirements. This could take a while.
#9 125.3   Downloading tensorboard-2.16.2-py3-none-any.whl (5.5 MB)
#9 125.4      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 71.3 MB/s eta 0:00:00
#9 125.7   Downloading tensorboard-2.16.1-py3-none-any.whl (5.5 MB)
#9 125.8      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 205.2 MB/s eta 0:00:00
#9 125.8 Collecting tf-keras>=2.15.0 (from tensorboard->-r requirements.txt (line 154))
#9 125.8   Downloading tf_keras-2.18.0-py3-none-any.whl (1.7 MB)
#9 125.8      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 234.0 MB/s eta 0:00:00
#9 126.1 Collecting tensorboard (from -r requirements.txt (line 154))
#9 126.2   Downloading tensorboard-2.16.0-py3-none-any.whl (5.5 MB)
#9 126.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 227.9 MB/s eta 0:00:00
#9 126.5 Collecting tf-keras-nightly (from tensorboard->-r requirements.txt (line 154))
#9 126.5   Downloading tf_keras_nightly-2.19.0.dev2024112210-py3-none-any.whl (1.7 MB)
#9 126.5      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 176.7 MB/s eta 0:00:00
#9 126.8 Collecting tensorboard (from -r requirements.txt (line 154))
#9 126.8   Downloading tensorboard-2.15.2-py3-none-any.whl (5.5 MB)
#9 126.8      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 291.7 MB/s eta 0:00:00
#9 126.9 Collecting google-auth<3,>=1.6.3 (from tensorboard->-r requirements.txt (line 154))
#9 126.9   Downloading google_auth-2.36.0-py2.py3-none-any.whl (209 kB)
#9 126.9      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 209.5/209.5 kB 274.9 MB/s eta 0:00:00
#9 126.9 Collecting google-auth-oauthlib<2,>=0.5 (from tensorboard->-r requirements.txt (line 154))
#9 127.0   Downloading google_auth_oauthlib-1.2.1-py2.py3-none-any.whl (24 kB)
#9 127.2 Collecting tensorboard (from -r requirements.txt (line 154))
#9 127.2   Downloading tensorboard-2.15.1-py3-none-any.whl (5.5 MB)
#9 127.3      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 147.1 MB/s eta 0:00:00
#9 127.3   Downloading tensorboard-2.15.0-py3-none-any.whl (5.6 MB)
#9 127.4      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.6/5.6 MB 45.8 MB/s eta 0:00:00
#9 127.5   Downloading tensorboard-2.14.1-py3-none-any.whl (5.5 MB)
#9 127.5      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 281.1 MB/s eta 0:00:00
#9 127.5 Collecting google-auth-oauthlib<1.1,>=0.5 (from tensorboard->-r requirements.txt (line 154))
#9 127.5   Downloading google_auth_oauthlib-1.0.0-py2.py3-none-any.whl (18 kB)
#9 127.9 INFO: pip is looking at multiple versions of tensorboard to determine which version is compatible with other requirements. This could take a while.
#9 127.9 Collecting tensorboard (from -r requirements.txt (line 154))
#9 127.9   Downloading tensorboard-2.14.0-py3-none-any.whl (5.5 MB)
#9 127.9      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 292.5 MB/s eta 0:00:00
#9 128.2 INFO: This is taking longer than usual. You might need to provide the dependency resolver with stricter constraints to reduce runtime. See https://pip.pypa.io/warnings/backtracking for guidance. If you want to abort this run, press Ctrl + C.
#9 128.2   Downloading tensorboard-2.13.0-py3-none-any.whl (5.6 MB)
#9 128.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.6/5.6 MB 244.8 MB/s eta 0:00:00
#9 128.6   Downloading tensorboard-2.12.3-py3-none-any.whl (5.6 MB)
#9 128.6      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.6/5.6 MB 215.5 MB/s eta 0:00:00
#9 128.9   Downloading tensorboard-2.12.2-py3-none-any.whl (5.6 MB)
#9 128.9      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.6/5.6 MB 191.9 MB/s eta 0:00:00
#9 129.0 Collecting tensorboard-plugin-wit>=1.6.0 (from tensorboard->-r requirements.txt (line 154))
#9 129.0   Downloading tensorboard_plugin_wit-1.8.1-py3-none-any.whl (781 kB)
#9 129.0      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 781.3/781.3 kB 262.7 MB/s eta 0:00:00
#9 129.3 Collecting tensorboard (from -r requirements.txt (line 154))
#9 129.3   Downloading tensorboard-2.12.1-py3-none-any.whl (5.6 MB)
#9 129.4      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.6/5.6 MB 60.8 MB/s eta 0:00:00
#9 129.7   Downloading tensorboard-2.12.0-py3-none-any.whl (5.6 MB)
#9 129.7      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.6/5.6 MB 210.8 MB/s eta 0:00:00
#9 129.8 Collecting google-auth-oauthlib<0.5,>=0.4.1 (from tensorboard->-r requirements.txt (line 154))
#9 129.8   Downloading google_auth_oauthlib-0.4.6-py2.py3-none-any.whl (18 kB)
#9 130.1 Collecting tensorboard (from -r requirements.txt (line 154))
#9 130.1   Downloading tensorboard-2.11.2-py3-none-any.whl (6.0 MB)
#9 130.1      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.0/6.0 MB 166.8 MB/s eta 0:00:00
#9 130.1   Downloading tensorboard-2.11.0-py3-none-any.whl (6.0 MB)
#9 130.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.0/6.0 MB 206.9 MB/s eta 0:00:00
#9 130.2   Downloading tensorboard-2.10.1-py3-none-any.whl (5.9 MB)
#9 130.3      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.9/5.9 MB 104.5 MB/s eta 0:00:00
#9 130.3   Downloading tensorboard-2.10.0-py3-none-any.whl (5.9 MB)
#9 130.5      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.9/5.9 MB 34.9 MB/s eta 0:00:00
#9 130.5   Downloading tensorboard-2.9.1-py3-none-any.whl (5.8 MB)
#9 130.5      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.8/5.8 MB 222.9 MB/s eta 0:00:00
#9 130.5   Downloading tensorboard-2.9.0-py3-none-any.whl (5.8 MB)
#9 130.6      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.8/5.8 MB 101.2 MB/s eta 0:00:00
#9 130.6   Downloading tensorboard-2.8.0-py3-none-any.whl (5.8 MB)
#9 130.7      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.8/5.8 MB 219.0 MB/s eta 0:00:00
#9 130.7   Downloading tensorboard-2.7.0-py3-none-any.whl (5.8 MB)
#9 130.7      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.8/5.8 MB 243.5 MB/s eta 0:00:00
#9 130.8   Downloading tensorboard-2.6.0-py3-none-any.whl (5.6 MB)
#9 131.0      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.6/5.6 MB 35.5 MB/s eta 0:00:00
#9 131.0 Collecting google-auth<2,>=1.6.3 (from tensorboard->-r requirements.txt (line 154))
#9 131.0   Downloading google_auth-1.35.0-py2.py3-none-any.whl (152 kB)
#9 131.0      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 152.9/152.9 kB 274.6 MB/s eta 0:00:00
#9 131.0 Collecting tensorboard (from -r requirements.txt (line 154))
#9 131.0   Downloading tensorboard-2.5.0-py3-none-any.whl (6.0 MB)
#9 131.1      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.0/6.0 MB 58.4 MB/s eta 0:00:00
#9 131.2   Downloading tensorboard-2.4.1-py3-none-any.whl (10.6 MB)
#9 131.3      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.6/10.6 MB 150.1 MB/s eta 0:00:00
#9 131.7   Downloading tensorboard-2.4.0-py3-none-any.whl (10.6 MB)
#9 131.8      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.6/10.6 MB 129.9 MB/s eta 0:00:00
#9 132.1   Downloading tensorboard-2.3.0-py3-none-any.whl (6.8 MB)
#9 132.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.8/6.8 MB 183.9 MB/s eta 0:00:00
#9 132.6   Downloading tensorboard-2.2.2-py3-none-any.whl (3.0 MB)
#9 132.6      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 85.6 MB/s eta 0:00:00
#9 133.0   Downloading tensorboard-2.2.1-py3-none-any.whl (3.0 MB)
#9 133.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 19.8 MB/s eta 0:00:00
#9 133.6   Downloading tensorboard-2.2.0-py3-none-any.whl (2.8 MB)
#9 133.6      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.8/2.8 MB 254.7 MB/s eta 0:00:00
#9 134.0   Downloading tensorboard-2.1.1-py3-none-any.whl (3.8 MB)
#9 134.0      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 47.8 MB/s eta 0:00:00
#9 134.5   Downloading tensorboard-2.1.0-py3-none-any.whl (3.8 MB)
#9 134.7      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 21.9 MB/s eta 0:00:00
#9 135.1   Downloading tensorboard-2.0.2-py3-none-any.whl (3.8 MB)
#9 135.3      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 24.6 MB/s eta 0:00:00
#9 135.7   Downloading tensorboard-2.0.1-py3-none-any.whl (3.8 MB)
#9 135.9      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 20.0 MB/s eta 0:00:00
#9 136.6   Downloading tensorboard-2.0.0-py3-none-any.whl (3.8 MB)
#9 136.8      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 16.7 MB/s eta 0:00:00
#9 137.2   Downloading tensorboard-1.15.0-py3-none-any.whl (3.8 MB)
#9 137.3      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 38.8 MB/s eta 0:00:00
#9 137.7   Downloading tensorboard-1.14.0-py3-none-any.whl (3.1 MB)
#9 137.7      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 178.9 MB/s eta 0:00:00
#9 138.1   Downloading tensorboard-1.13.1-py3-none-any.whl (3.2 MB)
#9 138.1      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.2/3.2 MB 195.9 MB/s eta 0:00:00
#9 138.6   Downloading tensorboard-1.13.0-py3-none-any.whl (3.2 MB)
#9 138.8      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.2/3.2 MB 15.2 MB/s eta 0:00:00
#9 139.2   Downloading tensorboard-1.12.2-py3-none-any.whl (3.0 MB)
#9 139.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 217.7 MB/s eta 0:00:00
#9 139.7   Downloading tensorboard-1.12.1-py3-none-any.whl (3.0 MB)
#9 139.9      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 20.6 MB/s eta 0:00:00
#9 140.3   Downloading tensorboard-1.12.0-py3-none-any.whl (3.0 MB)
#9 140.5      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 20.6 MB/s eta 0:00:00
#9 140.9   Downloading tensorboard-1.11.0-py3-none-any.whl (3.0 MB)
#9 141.0      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 20.8 MB/s eta 0:00:00
#9 141.5   Downloading tensorboard-1.10.0-py3-none-any.whl (3.3 MB)
#9 141.7      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 14.8 MB/s eta 0:00:00
#9 142.1   Downloading tensorboard-1.9.0-py3-none-any.whl (3.3 MB)
#9 142.4      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 15.0 MB/s eta 0:00:00
#9 142.8   Downloading tensorboard-1.8.0-py3-none-any.whl (3.1 MB)
#9 142.9      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 35.5 MB/s eta 0:00:00
#9 142.9 Collecting html5lib==0.9999999 (from tensorboard->-r requirements.txt (line 154))
#9 142.9   Downloading html5lib-0.9999999.tar.gz (889 kB)
#9 142.9      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 889.3/889.3 kB 257.8 MB/s eta 0:00:00
#9 143.0   Preparing metadata (setup.py): started
#9 143.2   Preparing metadata (setup.py): finished with status 'done'
#9 143.2 Collecting tensorboard (from -r requirements.txt (line 154))
#9 143.3   Downloading tensorboard-1.7.0-py3-none-any.whl (3.1 MB)
#9 143.6      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 10.1 MB/s eta 0:00:00
#9 143.6   Downloading tensorboard-1.6.0-py3-none-any.whl (3.0 MB)
#9 143.6      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 215.1 MB/s eta 0:00:00
#9 143.6 Collecting proto-plus (from -r requirements.txt (line 104))
#9 143.6   Downloading proto_plus-1.24.0-py3-none-any.whl (50 kB)
#9 143.6      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 50.1/50.1 kB 234.5 MB/s eta 0:00:00
#9 155.3   Downloading proto_plus-1.23.0-py3-none-any.whl (48 kB)
#9 155.3      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 48.8/48.8 kB 183.7 MB/s eta 0:00:00
#9 155.4 INFO: pip is looking at multiple versions of proto-plus to determine which version is compatible with other requirements. This could take a while.
#9 155.4   Downloading proto_plus-1.22.3-py3-none-any.whl (48 kB)
#9 155.4      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 48.1/48.1 kB 203.2 MB/s eta 0:00:00
#9 155.4   Downloading proto_plus-1.22.2-py3-none-any.whl (47 kB)
#9 155.4      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 47.9/47.9 kB 216.0 MB/s eta 0:00:00
#9 155.4   Downloading proto_plus-1.22.1-py3-none-any.whl (47 kB)
#9 155.4      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 47.9/47.9 kB 235.7 MB/s eta 0:00:00
#9 155.4   Downloading proto_plus-1.22.0-py3-none-any.whl (47 kB)
#9 155.4      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 47.7/47.7 kB 228.0 MB/s eta 0:00:00
#9 155.4   Downloading proto_plus-1.20.6-py3-none-any.whl (46 kB)
#9 155.4      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 46.4/46.4 kB 179.8 MB/s eta 0:00:00
#9 155.4   Downloading proto_plus-1.20.5-py3-none-any.whl (46 kB)
#9 155.4      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 46.4/46.4 kB 125.1 MB/s eta 0:00:00
#9 155.5   Downloading proto_plus-1.20.4-py3-none-any.whl (46 kB)
#9 155.5      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 46.4/46.4 kB 228.7 MB/s eta 0:00:00
#9 167.3 INFO: pip is looking at multiple versions of proto-plus to determine which version is compatible with other requirements. This could take a while.
#9 167.3 INFO: This is taking longer than usual. You might need to provide the dependency resolver with stricter constraints to reduce runtime. See https://pip.pypa.io/warnings/backtracking for guidance. If you want to abort this run, press Ctrl + C.
#9 167.3   Downloading proto_plus-1.20.3-py3-none-any.whl (46 kB)
#9 167.3      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 46.2/46.2 kB 218.0 MB/s eta 0:00:00
#9 178.7   Downloading proto_plus-1.20.2-py3-none-any.whl (45 kB)
#9 178.7      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 46.0/46.0 kB 200.4 MB/s eta 0:00:00
#9 190.5   Downloading proto_plus-1.20.1-py3-none-any.whl (45 kB)
#9 190.5      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45.9/45.9 kB 191.3 MB/s eta 0:00:00
#9 202.2   Downloading proto_plus-1.20.0-py3-none-any.whl (45 kB)
#9 202.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45.7/45.7 kB 195.4 MB/s eta 0:00:00
#9 214.0   Downloading proto_plus-1.19.9-py3-none-any.whl (45 kB)
#9 214.0      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45.5/45.5 kB 170.7 MB/s eta 0:00:00
#9 225.7   Downloading proto_plus-1.19.8-py3-none-any.whl (45 kB)
#9 225.7      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45.4/45.4 kB 207.5 MB/s eta 0:00:00
#9 237.4   Downloading proto_plus-1.19.7-py3-none-any.whl (45 kB)
#9 237.4      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45.4/45.4 kB 191.2 MB/s eta 0:00:00
#9 249.2   Downloading proto_plus-1.19.6-py3-none-any.whl (45 kB)
#9 249.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45.4/45.4 kB 205.9 MB/s eta 0:00:00
#9 260.9   Downloading proto_plus-1.19.5-py3-none-any.whl (44 kB)
#9 260.9      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.2/44.2 kB 215.6 MB/s eta 0:00:00
#9 272.7   Downloading proto_plus-1.19.4-py3-none-any.whl (44 kB)
#9 272.7      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.2/44.2 kB 215.9 MB/s eta 0:00:00
#9 284.5   Downloading proto_plus-1.19.3-py3-none-any.whl (44 kB)
#9 284.5      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.2/44.2 kB 186.1 MB/s eta 0:00:00
#9 296.3   Downloading proto_plus-1.19.2-py3-none-any.whl (43 kB)
#9 296.3      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.1/43.1 kB 204.5 MB/s eta 0:00:00
#9 308.1   Downloading proto_plus-1.19.1-py3-none-any.whl (43 kB)
#9 308.1      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.1/43.1 kB 158.5 MB/s eta 0:00:00
#9 319.9   Downloading proto_plus-1.19.0-py3-none-any.whl (42 kB)
#9 319.9      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.0/43.0 kB 208.8 MB/s eta 0:00:00
#9 331.6   Downloading proto_plus-1.18.1-py3-none-any.whl (42 kB)
#9 331.6      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.0/43.0 kB 188.0 MB/s eta 0:00:00
#9 343.1   Downloading proto_plus-1.18.0-py3-none-any.whl (42 kB)
#9 343.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.0/43.0 kB 213.2 MB/s eta 0:00:00
#9 355.0   Downloading proto_plus-1.17.0-py3-none-any.whl (42 kB)
#9 355.0      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.6/42.6 kB 202.1 MB/s eta 0:00:00
#9 366.9   Downloading proto_plus-1.16.0-py3-none-any.whl (42 kB)
#9 366.9      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.6/42.6 kB 193.6 MB/s eta 0:00:00
#9 378.7   Downloading proto_plus-1.15.0-py3-none-any.whl (42 kB)
#9 378.7      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.5/42.5 kB 208.8 MB/s eta 0:00:00
#9 390.5   Downloading proto_plus-1.14.2-py3-none-any.whl (42 kB)
#9 390.5      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.3/42.3 kB 207.9 MB/s eta 0:00:00
#9 402.2   Downloading proto-plus-1.13.0.tar.gz (44 kB)
#9 402.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.2/44.2 kB 179.7 MB/s eta 0:00:00
#9 402.2   Preparing metadata (setup.py): started
#9 402.4   Preparing metadata (setup.py): finished with status 'done'
#9 414.2   Downloading proto-plus-1.11.0.tar.gz (44 kB)
#9 414.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.0/44.0 kB 206.6 MB/s eta 0:00:00
#9 414.2   Preparing metadata (setup.py): started
#9 414.4   Preparing metadata (setup.py): finished with status 'done'
#9 425.9   Downloading proto-plus-1.10.2.tar.gz (42 kB)
#9 425.9      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.9/42.9 kB 195.3 MB/s eta 0:00:00
#9 425.9   Preparing metadata (setup.py): started
#9 426.1   Preparing metadata (setup.py): finished with status 'done'
#9 437.8   Downloading proto-plus-1.10.1.tar.gz (42 kB)
#9 437.8      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.9/42.9 kB 196.6 MB/s eta 0:00:00
#9 437.8   Preparing metadata (setup.py): started
#9 438.0   Preparing metadata (setup.py): finished with status 'done'
#9 449.7   Downloading proto-plus-1.10.0.tar.gz (24 kB)
#9 449.7   Preparing metadata (setup.py): started
#9 449.9   Preparing metadata (setup.py): finished with status 'done'
#9 461.6   Downloading proto-plus-1.9.1.tar.gz (23 kB)
#9 461.6   Preparing metadata (setup.py): started
#9 461.8   Preparing metadata (setup.py): finished with status 'done'
#9 473.5   Downloading proto-plus-1.9.0.tar.gz (24 kB)
#9 473.5   Preparing metadata (setup.py): started
#9 473.7   Preparing metadata (setup.py): finished with status 'done'
#9 485.4   Downloading proto-plus-1.8.1.tar.gz (23 kB)
#9 485.4   Preparing metadata (setup.py): started
#9 485.6   Preparing metadata (setup.py): finished with status 'done'
#9 497.3   Downloading proto-plus-1.8.0.tar.gz (24 kB)
#9 497.3   Preparing metadata (setup.py): started
#9 497.5   Preparing metadata (setup.py): finished with status 'done'
#9 508.9   Downloading proto-plus-1.7.1.tar.gz (23 kB)
#9 508.9   Preparing metadata (setup.py): started
#9 509.1   Preparing metadata (setup.py): finished with status 'done'
#9 520.9   Downloading proto-plus-1.7.0.tar.gz (23 kB)
#9 520.9   Preparing metadata (setup.py): started
#9 521.1   Preparing metadata (setup.py): finished with status 'done'
#9 532.8   Downloading proto-plus-1.6.0.tar.gz (23 kB)
#9 532.8   Preparing metadata (setup.py): started
#9 533.0   Preparing metadata (setup.py): finished with status 'done'
#9 544.7   Downloading proto-plus-1.5.3.tar.gz (23 kB)
#9 544.7   Preparing metadata (setup.py): started
#9 544.9   Preparing metadata (setup.py): finished with status 'done'
#9 556.6   Downloading proto-plus-1.5.2.tar.gz (23 kB)
#9 556.6   Preparing metadata (setup.py): started
#9 556.8   Preparing metadata (setup.py): finished with status 'done'
#9 568.5   Downloading proto-plus-1.5.1.tar.gz (23 kB)
#9 568.5   Preparing metadata (setup.py): started
#9 568.7   Preparing metadata (setup.py): finished with status 'done'
#9 580.4   Downloading proto-plus-1.4.0.tar.gz (23 kB)
#9 580.4   Preparing metadata (setup.py): started
#9 580.6   Preparing metadata (setup.py): finished with status 'done'
#9 592.1   Downloading proto_plus-1.3.2-py3-none-any.whl (39 kB)
#9 603.9   Downloading proto_plus-1.3.1-py3-none-any.whl (39 kB)
#9 615.7   Downloading proto_plus-1.3.0-py3-none-any.whl (39 kB)
#9 627.4   Downloading proto-plus-1.2.0.tar.gz (21 kB)
#9 627.4   Preparing metadata (setup.py): started
#9 627.6   Preparing metadata (setup.py): finished with status 'done'
#9 639.3   Downloading proto-plus-1.1.0.tar.gz (21 kB)
#9 639.3   Preparing metadata (setup.py): started
#9 639.5   Preparing metadata (setup.py): finished with status 'done'
#9 651.2   Downloading proto-plus-1.0.0.tar.gz (21 kB)
#9 651.2   Preparing metadata (setup.py): started
#9 651.4   Preparing metadata (setup.py): finished with status 'done'
#9 663.1   Downloading proto-plus-0.4.0.tar.gz (20 kB)
#9 663.1   Preparing metadata (setup.py): started
#9 663.3   Preparing metadata (setup.py): finished with status 'done'
#9 675.1   Downloading proto-plus-0.3.0.tar.gz (18 kB)
#9 675.1   Preparing metadata (setup.py): started
#9 675.2   Preparing metadata (setup.py): finished with status 'done'
#9 687.1   Downloading proto-plus-0.2.1.tar.gz (18 kB)
#9 687.1   Preparing metadata (setup.py): started
#9 687.3   Preparing metadata (setup.py): finished with status 'done'
#9 699.0   Downloading proto-plus-0.2.0.tar.gz (18 kB)
#9 699.0   Preparing metadata (setup.py): started
#9 699.2   Preparing metadata (setup.py): finished with status 'done'
#9 711.1   Downloading proto-plus-0.1.0.tar.gz (16 kB)
#9 711.1   Preparing metadata (setup.py): started
#9 711.3   Preparing metadata (setup.py): finished with status 'done'
#9 723.0 Collecting grpcio-tools (from -r requirements.txt (line 41))
#9 723.0   Downloading grpcio_tools-1.67.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.4 MB)
#9 723.0      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.4/2.4 MB 238.7 MB/s eta 0:00:00
#9 1306.4   Downloading grpcio_tools-1.67.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.4 MB)
#9 1306.5      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.4/2.4 MB 50.0 MB/s eta 0:00:00
""".splitlines()

output_file = "latest_downloaded_packages.py"
extract_last_versions_to_file(log_data, output_file)

print(f"Packages written to {output_file}")



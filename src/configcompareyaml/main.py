import argparse
from typing import Sequence
import yaml
import os

"""
This file will compare two YAML files, where --file1 is the developers configuration
file that does not get checked into GIT. The other YAML file, --file2, will be
the sample configuration file that does get checked into GIT. If your config files are
in a directory, just pull in the path to the files relative to the top directory

- repo: https://github.com/athertonsoftware/config-compare-yaml
    rev: v0.0.3
    hooks:
      - id: config-compare-yaml
        name: config-compare-yaml
        description: Compare the projects sample config keys to developers config file
        language: python
        language_version: 3.8.6
        additional_dependencies: [pyyaml]
        args:
          [
            "--file1=<path-to-file/>config.yaml",
            "--file2=<path-to-file/>config-sample.yaml",
          ]

or to run it locally from the .git/hooks directory

 - repo: local
    hooks:
      - id: config-compare-yaml
        name: config-compare-yaml
        description: Compare the projects sample config keys to developers config file
        language: python
        language_version: 3.8.6
        additional_dependencies: [pyyaml]
        entry: python .git/hooks/configcompareyaml.py
        args:
          [
            "--file1=<path-to-file/>config.yaml",
            "--file2=<path-to-file/>config-sample.yaml",
          ]

"""

def __getYamlFileKeys(fileName: str) -> list:
    # Get current working directory
    cwd = os.getcwd()
    #print(f"cwd: {cwd}")
    keys = []
    fullFilePath = cwd + "/" + fileName
    #print(f"localFilePath: {fullFilePath}")
    with open(fullFilePath, "r") as stream:
        try:
            data = yaml.safe_load(stream)
            for key in data:
                keys.append(key)
        except yaml.YAMLError as exc:
            print(exc)
    return keys

def __checkIfEqual(l1: list, l2: list) -> bool:
    l1.sort()
    l2.sort()
    if (l1 == l2):     
        return True
    else:
        return False        
  
def __parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--file1', type=str, 
        help='Developers config YAML file',
    )
    parser.add_argument(
        '--file2', type=str,
        help='Sample config YAML file',
    )
    parser.set_defaults(verbose=False)
    parser.add_argument('files', nargs=argparse.REMAINDER)
    return parser.parse_args()

def main(argv: Sequence[str] = None) -> int:
    args = __parse_arguments()
    configFile = args.file1
    configSampleFile = args.file2

    if not configFile:
        print(f"Missing config file")
        return 1
    elif not configSampleFile:
        print(f"Missing config sample file")
        return 1
    
    configKeys = __getYamlFileKeys(configFile)
    configSampleKeys = __getYamlFileKeys(configSampleFile)
    
    #print(f"Config keys: {configKeys}")
    #print(f"Config sample keys: {configSampleKeys}")

    isEqual = __checkIfEqual(configKeys, configSampleKeys)
    if (isEqual):
        print("Config files are same")
    else:
        missing = set(configKeys).difference(set(configSampleKeys))
        if missing:
            print(f"Missing values in {configSampleFile}: {missing}")
            return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

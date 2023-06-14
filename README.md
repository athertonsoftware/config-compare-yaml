<!--
Copyright 2023 Tony Akocs
SPDX-License-Identifier: MIT
-->
# config-compare-yaml
This pre-commit hook prevents commits when the specified YAML files contain different key values.

## Background:
Projects often contain a “config-sample.yaml” file that contains YAML-formatted example 
configurations for the project. When a developer wants to run the project, they just 
copy and change the “config-sample.yaml” file to “config.yaml”. The “config.yaml” file 
is used to build the project which will then contain their own specific configurations. 
The developer's custom “config.yaml” file is never checked into the repository, but 
the “config-sample.yaml” file is always checked into the repository. When a developer 
makes a change to the “config.yaml” file with a new key value, they often neglect to 
include it in the “config-sample.yaml” file. Following that, they commit all of their 
changes to the repository. Then, when you pull down their changes and build the 
application, you will get an error message that says "unknown property" or 
"property not found". Config-compare is utilized to prevent this situation.

# Description:
This pre-commit hook will compare two YAML configuration files. The comparison takes 
place between the developer’s custom “config.yaml” and the project’s 
“config-sample.yaml” file. If the “config-sample.yaml” file does not contain a key 
value that is in the developer’s config.yaml file, an error message will be displayed 
to the developer. The comparison is to prevent a developer’s custom config file from 
overwriting the project’s default config file template.

## Parameters
| Command Line    | Input                   | Description                                                    |
| --------------- | ----------------------- | -------------------------------------------------------------- |
| --file1         |  String file name       | The developers custom config file (example: config.yaml)       |
| --file2         |  String file name       | The project sample config file (example: config-sample.yaml)   |

## To Run:

```bash
# run in current directory
config-compare
# config-compare --file1 "config.yaml" --file2 "config-sample.yaml"

# run where the config files are in a directory (ex: deployment)
# config-compare --file1 "config.yaml" --file2 "config-sample.yaml"
```


## pre-commit
If you want to run it from Github use this configuration
```yaml
 - repo: https://github.com/akocs/config-compare-yaml
    rev: main
    hooks:
      - id: config-compare-yaml
        additional_dependencies: [pyyaml]
        always_run: true
        args:
          [
            "--file1=config.yaml",
            "--file2=config-sample.yaml",
          ]
```


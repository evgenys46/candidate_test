import yaml
import os

def split_services(config_file):
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)

    for service_name, params in config["service"].items():
        values = {}
        if "replicas" in params:
            values["replicaCount"] = params["replicas"]
        if "image" in params:
            image_repo, image_tag = params["image"].split(":")
            values["image"] = {
                "repository": image_repo,
                "tag": image_tag
            }
        if "storage" in params:
            values["storage"] = {"size": params["storage"]}

        with open(f"values_{service_name}.yml", "w") as out:
            yaml.dump(values, out)

if __name__ == "__main__":
    split_services("config.yaml")

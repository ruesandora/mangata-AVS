import json
import docker

from datetime import datetime

client = docker.from_env()  # Connect to the local Docker daemon

if __name__ == "__main__":

    # Replace with your actual container name
    container_name = "mangata-finalizer-node"
    container = client.containers.get(container_name)
    print("Script started!")
    print("Container State: ", container.attrs['State'])
    print("Container Config: ", container.attrs['Config'])

    while True:
        # We assume that container is already up and running
        # It is restarted if "connection is shut down" error is encountered in the logs
        if container.attrs['State']['Restarting'] == True or container.attrs['State']['Status'] == "restarting":
            pass  #  If state is restarting do nothing
        else:
            try:
                script_initalized = datetime.now()  #  Required to filter logs by time
                for line in container.logs(stream=True, follow=True, since=script_initalized):
                    decoded_line = line.decode('utf-8').strip().split("\t")
                    if len(decoded_line) > 1 and decoded_line[1] == "INFO":
                        try:  # Required to suppress errors raised by json package
                            message = json.loads(decoded_line[-1])
                            if "err" in message:
                                if message["err"] == "connection is shut down":
                                    print("Restart required!")
                                    print(decoded_line[0], message)
                                    container.restart()
                                    break
                                else:
                                    print(decoded_line[0], message)
                        except Exception as e:
                            pass

            except Exception as e:
                print(f"Error: {e}")
                break  #  Terminate

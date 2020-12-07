# Examples for py-controller-model

The provided dockerfile available from the docker registry `docker pull azocolo/py-controller-model-examples:latest` builds an alpine image with python installed. It has all of the examples copied to `/root/examples` and requirements installed already. You should be able to follow the example instructions even easier.

You should run this with `docker run -it --rm --name="py-cm-ex" azocolo/py-controller-model-examples:latest`. Then in your separate terminal window, run another instance of docker, but this time link it to the other container with `--link <existing-name>:<inside-alias>` as shown here: `docker run -it --rm --name="py-cm-ex2" --link "py-cm-ex:pycmex" azocolo/py-controller-model-examples:latest` to connect the two docker containers' networks together. 

Now in the examples, reference any server or uri as the first containers alias name, `pycmex` in this instance. 
For example, in the websocket API example, instead of connecting with `ws://0.0.0.0:7033`, you now connect with `ws://pycmex:7033`. Nifty!
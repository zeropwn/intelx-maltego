# intelx-maltego
Maltego Transforms for Intelligence X (intelx.io)

## Installation

**NOTES**: 

* The ["config"](https://github.com/zeropwn/intelx-maltego/tree/master/config) directory is required, do not delete it at any point except during uninstallation.
* You *cannot* include any whitespaces in any of the filepaths unless it's for the Python executable.

### What will be installed:


#### Transforms
* Intelligence X Emails Transform
* Intelligence X Search Transform
* Intelligence X URLs Transform
* Intelligence X Subdomains Transform
* Intelligence X Search Result Transform

#### Entities
* Intelligence X BTC Entity
* Intelligence X Credit Card Entity
* Intelligence X IBAN Entity
* Intelligence X MAC Address Entity
* Intelligence X Simhash Entity
* Intelligence X Storage ID Entity
* Intelligence X System ID Entity
* Intelligence X UUID Entity

### Requirements

* [intelx-0.4](https://github.com/IntelligenceX/SDK/tree/master/Python)
* [maltego-trx](https://github.com/paterva/maltego-trx)
* [python \>= 3](https://www.python.org/)
* [An Intelligence X API Key](https://intelx.io/product)

While the installation procedure is relatively straightforward, there are a few fundamental differences between Linux / Windows. Mainly, the location of the Python executable. The first step, is to ensure intelx-0.4 and maltego-trx are a part of your Python environment.

```
git clone https://github.com/IntelligenceX/SDK
pip install ./SDK/Python
```

Now we can go ahead with the download.

```
git clone https://github.com/zeropwn/intelx-maltego
cd intelx-maltego
pip install -r requirements.txt
```

Once we've ensured all the requirements are present, we can continue with the actual installation. In order to do that, simply run the install.py script, and follow the instructions.

![](https://i.imgur.com/mTYjpEg.png)

Now that we've generated the Maltego MTZ configuration file, we can use that to import all of the transforms hosted in this repository. It will be located within the intelx-maltego folder. 

Since that's done, all we have to do now is import that file in Maltego by going to Maltego > Import / Export > Import Configuration > Import intelx.mtz file

You should be met with a screen similar to this:

![](https://camo.githubusercontent.com/5e51005ed2eaf24bfa35068557a7f7a8fac833ee/68747470733a2f2f692e696d6775722e636f6d2f3658474b4b72752e706e67)


## Uninstallation

If you'd like to remove the entities and transforms from your Maltego installation, you must do so manually.

### Entity Removal

To remove the Intelligence X entities, simply navigate to Entities > Manage Entities > Search for "intelx", and click the "X" on the entities you'd like to remove.

![](https://i.imgur.com/5xpoXbr.png)

### Transform Removal

To remove the Intelligence X transforms, simply navigate to Transforms > Transform Manager, then search for "Intelligence" and select all transforms, then right click > Delete.

![](https://i.imgur.com/dkWbq1Q.png)

From there, all you have to do is remove the intelx-maltego directory, and you should be good. Alternatively, you can do a factory reset, and remove all entities + transforms automatically.

![](https://i.imgur.com/ze6nDkm.png)


## Updating the transforms

At the time of writing, there is not an automatic update feature. If you need to update the code, simply remove the existing transforms, entities and transform bindings, and start the installation again.

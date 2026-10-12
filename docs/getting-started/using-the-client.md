# Using the client

## First instanatiate a `client` object

The `client` object provides access to methods that make it easy to query the LEDGER database.
First, import the `Client` class from `ledgerdata` and instantiate an object:

The `client` object lets you query the LEDGER database. First, import `Client()` and then create an object:

```python
from ledgerdata import Client

client = Client()
```

You can then use the `client`’s methods to query the database with a pattern like this `client.method()`.

Next we will walk you through some of the ways you can query the database to retrieve data.

---
 
## Actors 

Actors refers to any:

* adm0: nation
* adm1: state / province
* adm2: city


### List all actors

The following will return a dataframe with all the actors in the database:

```python
df_actors = client.get_all_actors()
```

### Parts of an actor

sometimes you want parts of an actor
```python
df_parts = client.parts(actor_id="US")
```

## Retrieve contextual data

Once you know the ids of the actors you are interested in you can easily retrieve contexual data on the actor. 
Keep in mind that not all contexual data is available for each actor. 

!!! note 
    unlike emissions, we only provide one datasource for each actor.

### Emission targets

```python
list_of_ids=["CA", "US", "GB"]

df = client.targets(actor_id=list_of_ids)
```
### Population

```python
list_of_ids=["CA", "US", "GB"]

df = client.population(actor_id=list_of_ids)
```

### GDP

```python
list_of_ids=["CA", "US", "GB"]

df = client.gdp(actor_id=list_of_ids)
```

### Energy Consumption

```python
list_of_ids=["CA", "US", "GB"]

df = client.energy_consumption(actor_id=list_of_ids)
```


---


## Emissions 

Where possible, emissions are broken down into subsector and gas and aggregated using global warming potentials (GWP).

### Total emissions

```python
list_of_actors = ["CA", "US", "GB"]

df = client.emissions_total(actor_id=list_of_actors)
```

### Decompose emissions

You can retrieve emissions based on gas and sectors

```python

params = {
    actor_id: "CA",
    gas: "CH4",
    sector: "agriculture"
}

df = client.emissions_by(**params)
```


### Global Warming Potentials

You can retrieve global warming potentials from an assessement report

```python
df = client.gwp(assessment_report="AR5")
```

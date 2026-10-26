# %% [markdown]
# This notebook showcases some of the commands you can use with the ledgerdata python client

# %% [markdown]
# ## Instantiate a client object

# %%
from ledgerdata import Client
client = Client()

# %% [markdown]
# ## Show all actors

# %%
client.get_all_actors()

# %% [markdown]
# ## Show parts of an actor. Here I show parts of Canada

# %%
actor_id = "CA"
client.parts_of_actor(actor_id)

# %% [markdown]
# ## Get all the emissions from an actor

# %%
actor_id = "CA"
client.emissions(actor_id=actor_id)

# %% [markdown]
# ## can also get contextual data

# %%
client.gdp(actor_id)

# %%
client.population(actor_id)

# %%
client.targets(actor_id)

# %% [markdown]
# ## Show all datasources

# %%
client.datasource()

# %% [markdown]
# ## Show all global warming potentials

# %%
client.gwp()

# %% [markdown]
# ## show all sectors

# %%
client.sector()
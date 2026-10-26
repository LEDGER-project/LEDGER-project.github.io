# REST API

The [RESTful API](https://restfulapi.net/) is created with [FastAPI](https://fastapi.tiangolo.com/) and [psycopg](https://www.psycopg.org/) and is provides low-level access to the database. The API (and database) is currently hosted with [DigitalOcean](https://www.digitalocean.com/). This REST API is mainly intended for web applications to query the database. If you are using LEDGER for data analysis we suggest using the Python Client. 

Here, we provide a brief overview of the API endpoints. The table below summarizes the LEDGER API endpoints used to query actors and associated datasets. `{actor_id}` denotes a path parameter representing the unique identifier of an actor (e.g., country, state, province, or city) in the LEDGER database. Countries, states, and provinces use ISO3 codes, while cities use LOCODE. 


| Endpoint | Description | Query Parameters |
|---|---|---|
| <code style="white-space: nowrap;">/actor</code> | List all actors in the database. | — |
| <code style="white-space: nowrap;">/actor/{actor_id}/parts</code> | List actors contained within another actor (e.g., states within a country). | `type` |
| <code style="white-space: nowrap;">/actor/{actor_id}/gdp</code> | Return GDP time series for a given actor. | — |
| <code style="white-space: nowrap;">/actor/{actor_id}/population</code> | Return population time series for a given actor. | — |
| <code style="white-space: nowrap;">/actor/{actor_id}/energy_consumption</code> | Return energy consumption time series for a given actor. | — |
| <code style="white-space: nowrap;">/actor/{actor_id}/targets</code> | Return emissions reduction targets associated with an actor. | — |
| <code style="white-space: nowrap;">/actor/{actor_id}/emissions</code> | Return greenhouse gas emissions time series. Results can be filtered by gas species, sector classification, or datasource. | <code style="white-space: nowrap;"> `datasource`<br>`sector`<br>`gas` </code>|
| <code style="white-space: nowrap;">/sector</code> | returns emission sectors | <code style="white-space: nowrap;">`taxonomy`<br>`code` </code>|
| <code style="white-space: nowrap;">/gwp</code> | returns global warming potential | <code style="white-space: nowrap;"> `assessment_report`<br>`gas`<br>`time_horizon` </code>|
| <code style="white-space: nowrap;">/datasource</code> | returns global warming potential | <code style="white-space: nowrap;"> `name`<br>`publisher` </code>|

For complete documentation please see the API documentation in ReDOC and Swagger format below.

[ReDOC Documentation](https://orca-app-5ivtt.ondigitalocean.app/redoc){ .md-button .md-button--primary }
[Swagger Documentation](https://orca-app-5ivtt.ondigitalocean.app/docs){ .md-button .md-button--primary }

## Usage

The API provides endpoints to retrieve emissions and contextual data.

!!! example

    The following returns all the actors in the database [https://orca-app-5ivtt.ondigitalocean.app/api/v0/actor](https://orca-app-5ivtt.ondigitalocean.app/api/v0/actor).

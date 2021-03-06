# X8313  Betting Strategy & Simulation Code
The following is a code excerpt from X8313 Inc. and not necessarily fully functional. The purpose of this repo is only to showcase my work and not intended for use.

**Key Features**

* Performance Metrics & Built-In Caching
* DataBase Interfacing (using SQLAlchemy)
* Custom Strategy Integration (see "How To")

### Strategy Code
These are a set of Python functions that are used to define any possible strategy, given the exisiting data-points in the target data and a method for applying the strategy to a set of races. 

It's a simple, functional filtering framework.

### Simulator Code
This is a Python that is used to simulate any user-defined strategy across any time-period. It is built on top of SQLAlchemy, as our Data Lake was hosted on an AWS RDS (PostgreSQL) Database.

## How To
These 2 pieces interface seemlesly together. Here is some psuedo code to illustrate how it works:

```
datelist = list of dates
strategy_dict = Python dict of user-defined rules
Simulator(datelist, strategy_dict):
    return P&L
```

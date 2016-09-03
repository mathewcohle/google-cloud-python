# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Shortcut methods for getting set up with Google Cloud Datastore.

You'll typically use these to get started with the API::

    >>> from google.cloud import datastore
    >>>
    >>> client = datastore.Client()
    >>> key = client.key('EntityKind', 1234)
    >>> entity = datastore.Entity(key)
    >>> query = client.query(kind='EntityKind')

The main concepts with this API are:

- :class:`google.cloud.datastore.connection.Connection`
  which represents a connection between your machine and the Cloud Datastore
  API.

- :class:`google.cloud.datastore.client.Client`
  which represents a project (string) and namespace (string) bundled with
  a connection and has convenience methods for constructing objects with that
  project / namespace.

- :class:`google.cloud.datastore.entity.Entity`
  which represents a single entity in the datastore
  (akin to a row in relational database world).

- :class:`google.cloud.datastore.key.Key`
  which represents a pointer to a particular entity in the datastore
  (akin to a unique identifier in relational database world).

- :class:`google.cloud.datastore.query.Query`
  which represents a lookup or search over the rows in the datastore.

- :class:`google.cloud.datastore.transaction.Transaction`
  which represents an all-or-none transaction and enables consistency
  when race conditions may occur.
"""

from google.cloud.datastore.batch import Batch
from google.cloud.datastore.connection import Connection
from google.cloud.datastore.client import Client
from google.cloud.datastore.entity import Entity
from google.cloud.datastore.key import Key
from google.cloud.datastore.query import Query
from google.cloud.datastore.transaction import Transaction


SCOPE = Connection.SCOPE

# micropython-ijson

This is an attempt to port the ijson JSON tokenizer to Micropython environments.

It should help with the parsing of HTTP API results from low-memory platforms such as the ESP8622.

For example, the Openweathermap API produces forecast information in JSON like the openweathermap.json file provided in this repo. The main.py in this repo shows how ijson can be used to extract the rain forecast through tokenizing instead of full JSON unmarshalling.

Note: Work on this repository was halted given issues in regex support on Micropython. Work was then superceded by the [Medea Project](https://github.com/ShrimpingIt/medea) a new implementation of a bytewise JSON parser specifically targeting low memory environments and Micropython.

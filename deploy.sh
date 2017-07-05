PORT="/dev/ttyUSB0"
AMPY="ampy --port ${PORT}" 
$AMPY mkdir ijson
$AMPY mkdir ijson/backends
find ijson/ -name '*.py' | xargs -n1 -I{} $AMPY put {} {}
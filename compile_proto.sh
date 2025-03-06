echo [1/3] Copying files...
mkdir protos/client
mkdir protos/client/grpc_out
mkdir protos/game_server
mkdir protos/game_server/grpc_out
cp protos/game.proto protos/client/grpc_out
cp protos/game.proto protos/game_server/grpc_out

echo [2/3] Generating proto...
mkdir game_server/grpc_out
mkdir client/grpc_out
python -m grpc_tools.protoc --proto_path=./protos/ --python_out=. --grpc_python_out=. game_server/grpc_out/game.proto
python -m grpc_tools.protoc --proto_path=./protos/ --python_out=. --grpc_python_out=. client/grpc_out/game.proto

echo [3/3] Removing files...
rm -rf protos/client
rm -rf protos/game_server

echo Competed!
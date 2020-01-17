@echo off

echo [1/3] Copying files...
mkdir protos\client\grpc_out
mkdir protos\game_server\grpc_out
copy protos\game.proto protos\client\grpc_out
copy protos\game.proto protos\game_server\grpc_out

echo [2/3] Generating proto...
python -m grpc_tools.protoc --proto_path=./protos/ --python_out=. --grpc_python_out=. game_server/grpc_out/game.proto
python -m grpc_tools.protoc --proto_path=./protos/ --python_out=. --grpc_python_out=. client/grpc_out/game.proto

echo [3/3] Removing files...
rmdir protos\client /s /q
rmdir protos\game_server /s /q

echo Competed!
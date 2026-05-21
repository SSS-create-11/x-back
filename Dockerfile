# 1. ベースにするOS（Pythonが入ってる軽量版を選ぶわん）
FROM python:3.9-slim

# 2. コンテナの中の作業場所を決めるわん
WORKDIR /app

# 3. 今いる場所のファイルを、コンテナの中の /app にコピーするわん
COPY app.py .

# 4. コンテナが起動した時に実行するコマンドを指定するわん
CMD ["python", "app.py"]

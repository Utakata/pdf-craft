# 開発ガイド

## セットアップ

### 0. システムの依存関係 (WSL/Linux)

WSL または Linux で開発する場合は、最初に poppler-utils をインストールしてください：

```shell
sudo apt-get update
sudo apt-get install poppler-utils
```

インストールの確認：
```shell
pdfinfo --version
```

### 1. Python 環境の作成

Python 環境をセットアップします
```shell
python -m venv .venv
. ./.venv/bin/activate
```

### 2. 依存関係のインストール

#### オプション 1: クイックスタート (CPU 環境)

GPU のない macOS または Linux での迅速な開発セットアップ：

```shell
poetry run pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

これにより以下がインストールされます：
- 主要な依存関係 (PyMuPDF, doc-page-extractor, epub-generator)
- PyTorch CPU 版 (torch, torchvision)
- 開発用依存関係 (pylint)

#### オプション 2: CUDA 環境 (手動セットアップ)

CUDA 環境の場合は、正しい CUDA バージョンを確実にするために、最初に PyTorch を手動でインストールする必要があります。

##### ステップ 1: CUDA 付き PyTorch のインストール

CUDA 11.8 の場合：
```shell
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

CUDA 12.1 の場合：
```shell
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

CUDA 12.4 の場合：
```shell
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```

##### ステップ 2: プロジェクトの依存関係のインストール

```shell
poetry install
```

これにより以下がインストールされます：
- 主要な依存関係 (PyMuPDF, doc-page-extractor, epub-generator)
- 開発用依存関係 (pylint)

**なぜ CUDA の場合は手動セットアップが必要なのですか？**
- Poetry は 1 つのロックファイル内で複数の PyTorch ソースを処理できません
- CUDA バージョンごとに異なる PyTorch ビルドが必要です
- 最初に PyTorch をインストールすることで、ハードウェアに適した正しい CUDA バージョンを確実に使用できます

### 3. インストールの確認

PyTorch が正しくインストールされているか確認します：

```shell
python -c "import torch; print(f"PyTorch version: {torch.__version__}"); print(f"CUDA available: {torch.cuda.is_available()}")"
```

CPU 環境での期待される出力：
```
PyTorch version: 2.5.x+cpu
CUDA available: False
```

CUDA 環境での期待される出力：
```
PyTorch version: 2.5.x+cu121
CUDA available: True
```

## 開発ワークフロー

### テストの実行

```shell
poetry run python test.py
```

### リンターの実行

pylint でコード品質をチェックします：

```shell
python lint.py
```

または直接実行：

```shell
poetry run pylint pdf_craft
```

### パッケージのビルド

古いビルドをクリーンアップし、配布用ファイルを作成します：

```shell
python build.py
```

## プルリクエスト（PR）送信前

すべてのチェックがパスすることを確認してください：

```shell
poetry run python test.py
python lint.py
```

## 注意点

- 公開されるパッケージには依存関係として torch/torchvision は含まれていません
- エンドユーザーはそれぞれの環境に合わせて torch/torchvision を別途インストールする必要があります
- 開発時は、`poetry install` を実行する前に必ず PyTorch をインストールしてください

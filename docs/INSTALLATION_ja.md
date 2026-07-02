# インストールガイド

## システム要件

- Python >= 3.10, < 3.14 (3.11.16 推奨)
- Poppler (PDF の解析とレンダリングに必要)
- CUDA 11.8 または 12.1 をサポートする NVIDIA GPU
- 16 GB 以上の VRAM (24 GB 以上を推奨、詳細は [DeepSeek OCR Hardware Requirements Discussion](https://huggingface.co/deepseek-ai/DeepSeek-OCR/discussions/31) を参照)

## インストール手順

本プロジェクトはドキュメント認識に DeepSeek OCR を使用しており、**CUDA 環境での実行が必須**です。実際に PDF 変換のために pdf-craft を使用する場合は、以下の CUDA 環境のインストール手順に従ってください。

コードの開発、IDE の型ヒントの取得、またはソースコードの閲覧のみが必要な場合は、代替手段として CPU 環境のインストールを選択できますが、実際の OCR 認識を実行することはできません。

### CUDA 環境のインストール (推奨)

#### 1. CUDA 環境の構成

NVIDIA ドライバーと CUDA がインストールされていることを確認してください。CUDA バージョンを確認するには：

```bash
nvidia-smi
```

#### 2. PyTorch のインストール

OS と CUDA バージョンに基づいて、適切なインストールコマンドを選択してください。

[PyTorch 公式インストールページ](https://pytorch.org/get-started/locally/) にアクセスして、対応する構成を選択し、PyTorch をインストールしてください。

**例** (CUDA 12.1)：

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

#### 3. pdf-craft のインストール

```bash
pip install pdf-craft
```

#### 4. Poppler のインストール

pdf-craft は PDF の解析とレンダリングに（`pdf2image` を介して）Poppler を使用します。Poppler を別途インストールする必要があります：

**Ubuntu/Debian:**
```bash
sudo apt-get install poppler-utils
```

**macOS:**
```bash
brew install poppler
```

**Windows:**

[oschwartz10612/poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases/) から最新の Poppler バイナリをダウンロードし、`bin/` ディレクトリをシステムの PATH に追加してください。あるいは、pdf-craft の使用時に Poppler のパスを指定することもできます（[カスタム PDF ハンドラー](../README_ja.md#カスタム-pdf-ハンドラー) を参照）。

#### 5. インストールの確認

CUDA の確認：
```bash
python -c "import torch; print("CUDA available:", torch.cuda.is_available())"
```

`CUDA available: True` と出力されるはずです。

Poppler の確認：
```bash
pdfinfo -v
```

Poppler のバージョン情報が出力されるはずです。コマンドが見つからない場合は、上記の Poppler インストール手順を再度確認してください。

### CPU 環境のインストール (開発のみ)

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install pdf-craft
```

**注意:** 開発専用のセットアップであっても、PDF 関連の機能をテストしたい場合は、上記の手順 4 に従って Poppler をインストールする必要があります。

## トラブルシューティング

### Poppler Not Found エラー

pdf-craft の実行時に "Poppler not found in PATH" のようなエラーが発生した場合、Poppler が正しくインストールまたは構成されていないことを意味します：

1. **Poppler がインストールされていない** - お使いの OS に合わせた上記の Poppler インストール手順に従ってください。
2. **Poppler が PATH にない** (Windows) - Poppler の `bin/` ディレクトリをシステムの PATH に追加するか、`pdf_handler` パラメータを使用してパスを指定してください（[カスタム PDF ハンドラー](../README_ja.md#カスタム-pdf-ハンドラー) を参照）。
3. **間違ったパッケージがインストールされている** (Linux) - `poppler` ではなく、`poppler-utils` をインストールしたことを確認してください。

### CUDA Not Available エラー

pdf-craft を使用しようとした際に、以下のような RuntimeWarning が表示される場合：

```
CUDA is not available! This package requires CUDA to run,
but torch.cuda.is_available() returned False.
```

これは CUDA 環境が正しく構成されていないことを示しています。考えられる理由：

1. **CPU 版の PyTorch がインストールされている** - 上記の CUDA 環境のインストール手順に従って、CUDA サポート付きの PyTorch を再インストールする必要があります。
2. **NVIDIA ドライバーが古い、またはインストールされていない** - [NVIDIA ドライバーダウンロードページ](https://www.nvidia.com/download/index.aspx) にアクセスしてドライバーを更新してください。
3. **CUDA 対応の GPU がない** - 本プロジェクトの実行には NVIDIA GPU が必須です。

`nvidia-smi` コマンドを実行して、システムの GPU とドライバーの状態を確認できます。

### CUDA バージョンの選び方

1. `nvidia-smi` を実行し、右上の CUDA Version を確認します。
2. [PyTorch 公式サイト](https://pytorch.org/get-started/locally/) にアクセスし、対応する、またはそれより低い CUDA バージョンを選択します。
3. 通常、CUDA 12.1 または 11.8 が最も高い互換性を持っています。

### 依存関係の競合

依存関係のバージョン競合が発生した場合は、仮想環境の使用をお勧めします：

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# または
venv\\Scripts\\activate  # Windows

# その後、上記の CUDA 環境のインストール手順に従います
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
pip install pdf-craft
```

<div align=center>
  <h1>PDF Craft</h1>
  <p>
    <a href="https://github.com/oomol-lab/pdf-craft/actions/workflows/merge-build.yml" target="_blank"><img src="https://img.shields.io/github/actions/workflow/status/oomol-lab/pdf-craft/merge-build.yml" alt="ci" /></a>
    <a href="https://pypi.org/project/pdf-craft/" target="_blank"><img src="https://img.shields.io/badge/pip_install-pdf--craft-blue" alt="pip install pdf-craft" /></a>
    <a href="https://pypi.org/project/pdf-craft/" target="_blank"><img src="https://img.shields.io/pypi/v/pdf-craft.svg" alt="pypi pdf-craft" /></a>
    <a href="https://pypi.org/project/pdf-craft/" target="_blank"><img src="https://img.shields.io/pypi/pyversions/pdf-craft.svg" alt="python versions" /></a>
    <a href="https://deepwiki.com/oomol-lab/pdf-craft" target="_blank"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki" /></a>
    <a href="https://github.com/oomol-lab/pdf-craft/blob/main/LICENSE" target="_blank"><img src="https://img.shields.io/github/license/oomol-lab/pdf-craft" alt="license" /></a>
  </p>
  <p><a href="https://trendshift.io/repositories/15538" target="_blank"><img src="https://trendshift.io/api/badge/repositories/15538" alt="oomol-lab%2Fpdf-craft | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a></p>
  <p><a href="./README.md">English</a> | <a href="./README_zh-CN.md">中文</a> | 日本語</p>
</div>

## はじめに

pdf-craft は、PDF ファイルを様々なフォーマットに変換するツールです。特にスキャンされた書籍の PDF 処理に特化しています。

本プロジェクトは、ドキュメント認識に [DeepSeek OCR](https://github.com/deepseek-ai/DeepSeek-OCR) を使用しています。表や数式などの複雑なコンテンツの認識に対応しています。GPU アクセラレーションを利用することで、pdf-craft は PDF から Markdown または EPUB への変換プロセス全体をローカルで完結させることができます。変換中、pdf-craft はドキュメント構造を自動的に識別し、本文を正確に抽出すると同時に、ヘッダーやフッターなどの不要な要素を除去します。脚注、数式、表を含む学術・技術文書についても適切に処理し、これらの重要な要素（脚注内の画像などのアセットを含む）を保持します。EPUB への変換時には目次が自動的に生成されます。最終的に生成される Markdown または EPUB ファイルは、元の書籍の内容の完全性と可読性を維持します。

## 軽量かつ高速

正式版 v1.0.0 以降、pdf-craft は [DeepSeek OCR](https://github.com/deepseek-ai/DeepSeek-OCR) を全面的に採用し、テキスト補正のための LLM への依存を排除しました。この変更により、パフォーマンスが大幅に向上しました。変換プロセス全体がネットワークリクエストなしでローカルで完了するため、旧バージョンで見られた長い待ち時間やネットワークエラーが発生しなくなりました。

ただし、新しいバージョンでは LLM によるテキスト補正機能が削除されています。この機能が引き続き必要な場合は、旧バージョンの [v0.2.8](https://github.com/oomol-lab/pdf-craft/tree/v0.2.8) をご利用ください。

### オンライン版

ローカル環境を構築せずに pdf-craft を試してみたい場合は、[Inkora - PDF Craft](https://inkora.oomol.com/pdf-craft/) をお試しください。これは同じ PDF 変換ワークフローを使用して構築されたオンラインアプリケーションです。ブラウザ上で直接 PDF ファイルをアップロードして、主な機能を体験できます。

[![PDF Craft オンライン版](docs/images/website-en.png)](https://inkora.oomol.com/pdf-craft/)

## クイックスタート

### インストール

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install pdf-craft
```

上記のコマンドはクイックセットアップ用です。実際に pdf-craft を使用するには、PDF の解析とレンダリングのために **Poppler のインストール**（全ユースケースで必要）と、OCR 認識のために **CUDA 環境の設定**（実際の変換で必要）が必要です。詳細な手順については、[インストールガイド](docs/INSTALLATION_ja.md) を参照してください。

### 使い方

#### Markdown への変換

```python
from pdf_craft import transform_markdown

transform_markdown(
    pdf_path="input.pdf",
    markdown_path="output.md",
    markdown_assets_path="images",
)
```

![mdmd](docs/images/pdf2md-en.png)

#### EPUB への変換

```python
from pdf_craft import transform_epub, BookMeta

transform_epub(
    pdf_path="input.pdf",
    epub_path="output.epub",
    book_meta=BookMeta(
        title="書名",
        authors=["著者"],
    ),
)
```

![20251218-162533](docs/images/pdf2epub-en.png)

## 詳細な使い方

### Markdown への変換

```python
from pdf_craft import transform_markdown

transform_markdown(
    pdf_path="input.pdf",
    markdown_path="output.md",
    markdown_assets_path="images",
    analysing_path="temp",  # オプション：一時フォルダの指定
    ocr_size="gundam",  # オプション：tiny, small, base, large, gundam
    models_cache_path="models",  # オプション：モデルのキャッシュパス
    dpi=300,  # オプション：PDF ページレンダリングの DPI（デフォルト：300）
    max_page_image_file_size=None,  # オプション：最大画像ファイルサイズ（バイト）。超えた場合は自動的に DPI を調整
    includes_cover=False,  # オプション：カバーを含める
    includes_footnotes=True,  # オプション：脚注を含める
    ignore_pdf_errors=False,  # オプション：PDF レンダリングエラー時に続行
    ignore_ocr_errors=False,  # オプション：OCR 認識エラー時に続行
    generate_plot=False,  # オプション：可視化チャートの生成
    toc_llm=None,  # オプション：目次抽出を強化するための LLM インスタンス
    toc_assumed=False,  # オプション：目次ページが存在すると仮定するかどうか（デフォルト：False）
)
```

### EPUB への変換

```python
from pdf_craft import transform_epub, BookMeta, TableRender, LaTeXRender

transform_epub(
    pdf_path="input.pdf",
    epub_path="output.epub",
    analysing_path="temp",  # オプション：一時フォルダの指定
    ocr_size="gundam",  # オプション：tiny, small, base, large, gundam
    models_cache_path="models",  # オプション：モデルのキャッシュパス
    dpi=300,  # オプション：PDF ページレンダリングの DPI（デフォルト：300）
    max_page_image_file_size=None,  # オプション：最大画像ファイルサイズ（バイト）。超えた場合は自動的に DPI を調整
    includes_cover=True,  # オプション：カバーを含める
    includes_footnotes=True,  # オプション：脚注を含める
    ignore_pdf_errors=False,  # オプション：PDF レンダリングエラー時に続行
    ignore_ocr_errors=False,  # オプション：OCR 認識エラー時に続行
    generate_plot=False,  # オプション：可視化チャートの生成
    toc_llm=None,  # オプション：目次抽出を強化するための LLM インスタンス
    toc_assumed=True,  # オプション：目次ページが存在すると仮定するかどうか（EPUB のデフォルト：True）
    book_meta=BookMeta(
        title="書名",
        authors=["著者1", "著者2"],
        publisher="出版社",
        language="ja",
    ),
    lan="ja",  # オプション：言語 (ja/en/zh)
    table_render=TableRender.HTML,  # オプション：表のレンダリング方法
    latex_render=LaTeXRender.MATHML,  # オプション：数式のレンダリング方法
    inline_latex=True,  # オプション：インライン LaTeX 式を保持
)
```

### モデル管理

pdf-craft は DeepSeek OCR モデルに依存しており、初回実行時に Hugging Face から自動的にダウンロードされます。`models_cache_path` と `local_only` パラメータを使用して、モデルの保存と読み込みの動作を制御できます。

#### モデルの事前ダウンロード

本番環境では、初回実行時のダウンロードを避けるために、事前にモデルをダウンロードしておくことをお勧めします。

```python
from pdf_craft import predownload_models

predownload_models(
    models_cache_path="models",  # モデルキャッシュディレクトリを指定
    revision=None,  # オプション：モデルのリビジョンを指定
)
```

#### モデルキャッシュパスの指定

デフォルトでは、モデルはシステムの Hugging Face キャッシュディレクトリにダウンロードされます。`models_cache_path` パラメータを使用して、キャッシュ場所をカスタマイズできます。

```python
from pdf_craft import transform_markdown

transform_markdown(
    pdf_path="input.pdf",
    markdown_path="output.md",
    models_cache_path="./my_models",  # カスタムモデルキャッシュディレクトリ
)
```

#### オフラインモード

モデルを事前にダウンロード済みの場合は、`local_only=True` を使用してネットワークからのダウンロードを無効にし、ローカルモデルのみを使用するように強制できます。

```python
from pdf_craft import transform_markdown

transform_markdown(
    pdf_path="input.pdf",
    markdown_path="output.md",
    models_cache_path="./my_models",
    local_only=True,  # ローカルモデルのみを使用し、ネットワークからダウンロードしない
)
```

## API リファレンス

### OCR モデル

`ocr_size` パラメータは `DeepSeekOCRSize` 型を受け取ります：

- `tiny` - 最小モデル、最高速
- `small` - 小規模モデル
- `base` - ベースモデル
- `large` - 大規模モデル
- `gundam` - 最大モデル、最高品質（デフォルト）

### 表のレンダリング方法

- `TableRender.HTML` - HTML 形式（デフォルト）
- `TableRender.CLIPPING` - クリッピング形式（元の PDF スキャンから表の画像を直接切り出す）

### 数式のレンダリング方法

- `LaTeXRender.MATHML` - MathML 形式（デフォルト）
- `LaTeXRender.SVG` - SVG 形式
- `LaTeXRender.CLIPPING` - クリッピング形式（元の PDF スキャンから数式の画像を直接切り出す）

### インライン LaTeX

`inline_latex` パラメータ（EPUB のみ、デフォルト：`True`）は、出力にインライン LaTeX 式を保持するかどうかを制御します。有効にすると、インラインの数学公式は LaTeX コードとして保持され、対応する EPUB リーダーでレンダリングできます。

### 目次検出

`toc_assumed` パラメータは、pdf-craft が目次の抽出をどのように処理するかを制御します：

- `False`（Markdown のデフォルト）：目次ページが存在しないと仮定します。変換プロセスでは、ドキュメントの見出しに基づいて目次を生成し、目次ページの検出や処理は行いません。
- `True`（EPUB のデフォルト）：目次ページが存在すると仮定します。変換プロセスでは統計分析を使用して目次ページを検出し、章の構造を抽出します。

複雑な章の階層を持つ書籍の場合、オプションの `toc_llm` パラメータを設定して LLM による章タイトルの分析を有効にすることで、より正確な目次階層の検出が可能になります。

#### LLM による目次抽出の強化

LLM 強化された目次抽出を使用するには、LLM インスタンスを構成する必要があります：

```python
from pdf_craft import transform_epub, BookMeta, LLM

# 目次抽出用の LLM を構成
toc_llm = LLM(
    key="your-api-key",
    url="https://api.openai.com/v1",  # または LLM プロバイダーの URL
    model="gpt-4",
    token_encoding="cl100k_base",
    timeout=60.0,
    retry_times=3,
    retry_interval_seconds=5.0,
)

transform_epub(
    pdf_path="input.pdf",
    epub_path="output.epub",
    toc_assumed=True,  # 目次検出を有効化
    toc_llm=toc_llm,  # LLM による章タイトルの分析を有効化
    book_meta=BookMeta(
        title="書名",
        authors=["著者"],
    ),
)
```

### カスタム PDF ハンドラー

デフォルトでは、pdf-craft は PDF の解析とレンダリングに（`pdf2image` を介して）Poppler を使用します。Poppler がシステムの PATH にない場合は、カスタムパスを指定できます。

```python
from pdf_craft import transform_markdown, DefaultPDFHandler

# カスタム Poppler パスを指定
transform_markdown(
    pdf_path="input.pdf",
    markdown_path="output.md",
    pdf_handler=DefaultPDFHandler(poppler_path="/path/to/poppler/bin"),
)
```

指定しない場合、pdf-craft はシステムの PATH から Poppler を探します。高度なユースケースでは、`PDFHandler` プロトコルを実装して代替の PDF ライブラリを使用することもできます。

### エラー処理

`ignore_pdf_errors` および `ignore_ocr_errors` パラメータは、柔軟なエラー処理オプションを提供します。これらは 2 つの方法で使用できます：

**1. ブールモード** - 単純なオン/オフ制御：

```python
from pdf_craft import transform_markdown

transform_markdown(
    pdf_path="input.pdf",
    markdown_path="output.md",
    ignore_pdf_errors=True,  # すべての PDF レンダリングエラーを無視
    ignore_ocr_errors=True,  # すべての OCR 認識エラーを無視
)
```

`True` に設定すると、個別のページでエラーが発生しても処理を続行し、変換プロセス全体を停止する代わりにプレースホルダーメッセージを挿入します。

**2. カスタム関数モード** - きめ細かな制御：

```python
from pdf_craft import transform_markdown, OCRError, PDFError

def should_ignore_ocr_error(error: OCRError) -> bool:
    # 特定の種類の OCR エラーのみを無視する
    return error.kind == "recognition_failed"

def should_ignore_pdf_error(error: PDFError) -> bool:
    # どの PDF エラーを無視するかを決定するカスタムロジック
    return "timeout" in str(error)

transform_markdown(
    pdf_path="input.pdf",
    markdown_path="output.md",
    ignore_ocr_errors=should_ignore_ocr_error,  # カスタム関数を渡す
    ignore_pdf_errors=should_ignore_pdf_error,  # カスタム関数を渡す
)
```

これにより、変換プロセス中にどの特定のエラーを無視すべきかを決定するためのカスタムロジックを実装できます。

## 関連プロジェクト

- [EPUB Translator](https://github.com/oomol-lab/epub-translator)：pdf-craft で生成した EPUB をさらに二言語版に翻訳したい場合、EPUB Translator は元のレイアウト、画像、目次を保持したまま変換を行うことができます。詳細については、こちらの [デモビデオ](https://www.bilibili.com/video/BV1tMQZY5EYY/) をご覧ください。
- [SpineDigest](https://github.com/oomol-lab/spinedigest)：変換した書籍をさらに構造化されたダイジェストにまとめたい場合、SpineDigest は EPUB や Markdown から要約、章のトポロジー、知識グラフを生成できます。

## ライセンス

本プロジェクトは MIT ライセンスの下で公開されています。詳細は [LICENSE](./LICENSE) ファイルを参照してください。

v1.0.0 以降、pdf-craft は全面的に DeepSeek OCR（MIT ライセンス）に移行し、以前の AGPL-3.0 依存関係を削除したため、プロジェクト全体をより許容的な MIT ライセンスでリリースできるようになりました。なお、pdf-craft は DeepSeek OCR を介して easydict（LGPLv3 ライセンス）に間接的に依存しています。コミュニティのサポートと貢献に感謝いたします。

## 謝辞

- [DeepSeekOCR](https://github.com/deepseek-ai/DeepSeek-OCR)
- [doc-page-extractor](https://github.com/Moskize91/doc-page-extractor)
- [pyahocorasick](https://github.com/WojciechMula/pyahocorasick)

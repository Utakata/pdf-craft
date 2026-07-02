# リリースガイド

## 1. バージョンの更新

`pyproject.toml` 内のバージョン番号を更新します：

```toml
[tool.poetry]
version = "1.x.x"
```

## 2. 変更履歴 (Changelog) の更新

`docs/changelog/` 内に新しいバージョン用のファイル（例：`v1.x.x.md`）を作成し、主な変更内容を記述します。

## 3. コードのコミット

```bash
git add .
git commit -m "chore: release v1.x.x"
git push origin main
```

## 4. GitHub リリースの作成

GitHub のウェブインターフェースで新しいリリースを作成します：
- バージョン番号（例：`v1.x.x`）に対応する新しいタグを作成します。
- タイトルを `v1.x.x` に設定します。
- `docs/changelog/v1.x.x.md` の内容を説明欄にコピーします。

## 5. PyPI への公開

GitHub Actions によって、新しいタグがプッシュされると自動的に PyPI に公開されます。手動で公開する必要がある場合は、以下を実行します：

```bash
python build.py
poetry publish
```

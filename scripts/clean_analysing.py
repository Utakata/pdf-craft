#!/usr/bin/env python3
"""
清理 analysing 文件夹的脚本
删除除了 assets、ocr、plots 之外的所有文件和文件夹
"""

import argparse
import shutil
from pathlib import Path

_KEEP_FILES = {"assets", "ocr", "plots", "cover.png"}


def clean_analysing_folder():
    """删除 analysing 文件夹中除了指定目录之外的所有内容"""
    # 获取项目根目录
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    analysing_dir = project_root / "analysing"

    # 检查 analysing 目录是否存在
    if not analysing_dir.exists():
        print(f"❌ ディレクトリが存在しません: {analysing_dir}")
        return

    # 需要保留的目录

    print(f"📂 ディレクトリをクリーンアップ中: {analysing_dir}")
    print(f"🔒 保持するファイル: {', '.join(_KEEP_FILES)}")
    print()

    deleted_count = 0

    # 遍历 analysing 目录中的所有项
    for item in analysing_dir.iterdir():
        item_name = item.name

        # 跳过需要保留的目录
        if item_name in _KEEP_FILES:
            print(f"✅ 保持: {item_name}")
            continue

        # 删除文件或目录
        try:
            if item.is_dir():
                shutil.rmtree(item)
                print(f"🗑️  ディレクトリを削除: {item_name}")
            else:
                item.unlink()
                print(f"🗑️  ファイルを削除: {item_name}")
            deleted_count += 1
        except Exception as e:
            print(f"❌ {item_name} の削除に失敗しました: {e}")

    print()
    print(f"✨ クリーンアップ完了！合計 {deleted_count} 個の項目を削除しました")


if __name__ == "__main__":
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="analysing ディレクトリをクリーンアップします")
    parser.add_argument(
        "-y", "--yes", action="store_true", help="確認プロンプトをスキップして、直接クリーンアップを実行します"
    )
    args = parser.parse_args()

    # 确认操作
    if args.yes:
        clean_analysing_folder()
    else:
        response = input("⚠️  analysing ディレクトリをクリーンアップしてもよろしいですか？ (y/n): ")
        if response.lower() in ("y", "yes"):
            clean_analysing_folder()
        else:
            print("❌ 操作がキャンセルされました")

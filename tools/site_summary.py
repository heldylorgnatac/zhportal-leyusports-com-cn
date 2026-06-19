import json

SITE_DATA = {
    "url": "https://zhportal-leyusports.com.cn",
    "keywords": ["乐鱼体育"],
    "tags": ["体育资讯", "门户", "运动"],
    "description": "乐鱼体育官方门户网站，提供最新的体育新闻、赛事动态与综合体育信息服务。"
}

def format_summary(data: dict) -> str:
    lines = []
    lines.append("=" * 50)
    lines.append("站点摘要")
    lines.append("=" * 50)
    lines.append(f"URL: {data['url']}")
    lines.append(f"关键词: {', '.join(data['keywords'])}")
    lines.append(f"标签: {', '.join(data['tags'])}")
    lines.append(f"说明: {data['description']}")
    lines.append("-" * 50)
    return "\n".join(lines)

def export_as_json(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)

def export_as_markdown(data: dict) -> str:
    md = f"""# 站点摘要

- **URL**: {data['url']}
- **关键词**: {', '.join(data['keywords'])}
- **标签**: {', '.join(data['tags'])}
- **说明**: {data['description']}
"""
    return md

def validate_data(data: dict) -> bool:
    required = ["url", "keywords", "tags", "description"]
    for field in required:
        if field not in data:
            return False
        if not isinstance(data[field], (str, list)):
            return False
    if not isinstance(data["keywords"], list) or not isinstance(data["tags"], list):
        return False
    return True

def main():
    if not validate_data(SITE_DATA):
        print("数据验证失败，请检查站点资料结构。")
        return

    print("输出格式：plain / json / markdown")
    fmt = input("请选择输出格式（默认 plain）：").strip().lower() or "plain"

    if fmt == "json":
        output = export_as_json(SITE_DATA)
    elif fmt == "markdown":
        output = export_as_markdown(SITE_DATA)
    else:
        output = format_summary(SITE_DATA)

    print("\n" + output)

if __name__ == "__main__":
    main()
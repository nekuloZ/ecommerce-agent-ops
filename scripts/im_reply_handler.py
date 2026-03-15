#!/usr/bin/env python3
"""
IM 回复处理器 - 秘书使用此脚本识别用户回复并触发相应操作

用法:
    python3 im_reply_handler.py --task-id JJC-xxx --reply "通过"
    python3 im_reply_handler.py --task-id JJC-xxx --reply "补充：数据来源是飞书"
"""

import argparse
import json
import requests
import sys
from pathlib import Path

DASHBOARD_URL = "http://127.0.0.1:7892"

def detect_reply_type(reply: str):
    """检测回复类型"""
    reply = reply.strip().lower()
    
    # 审批关键词
    approve_keywords = ['通过', 'approve', '同意', 'ok', '好的', '可以', '准', '✅']
    reject_keywords = ['驳回', 'reject', '不同意', '退回', '修改', '❌', '不行']
    
    for kw in approve_keywords:
        if kw in reply:
            return 'approve', None
    
    for kw in reject_keywords:
        if kw in reply:
            return 'reject', None
    
    # 补充信息关键词
    if '补充' in reply or ':' in reply or '：' in reply:
        # 提取补充内容
        for sep in ['补充：', '补充:', '：', ':']:
            if sep in reply:
                content = reply.split(sep, 1)[-1].strip()
                if content:
                    return 'compliance-answer', content
    
    return None, None

def handle_im_reply(task_id: str, reply: str):
    """处理 IM 回复"""
    reply_type, content = detect_reply_type(reply)
    
    if reply_type == 'approve':
        # 调用审批 API
        resp = requests.post(
            f"{DASHBOARD_URL}/api/im-review",
            json={"taskId": task_id, "action": "通过"}
        )
        return resp.json()
    
    elif reply_type == 'reject':
        # 调用驳回 API
        resp = requests.post(
            f"{DASHBOARD_URL}/api/im-review",
            json={"taskId": task_id, "action": "驳回", "comment": content or "需要修改"}
        )
        return resp.json()
    
    elif reply_type == 'compliance-answer':
        # 调用补充信息 API
        resp = requests.post(
            f"{DASHBOARD_URL}/api/im-compliance-answer",
            json={"taskId": task_id, "answer": content}
        )
        return resp.json()
    
    else:
        return {"ok": False, "error": f"无法识别回复类型: {reply[:50]}"}

def main():
    parser = argparse.ArgumentParser(description='IM 回复处理器')
    parser.add_argument('--task-id', required=True, help='任务ID')
    parser.add_argument('--reply', required=True, help='用户回复内容')
    
    args = parser.parse_args()
    
    result = handle_im_reply(args.task_id, args.reply)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    if not result.get('ok'):
        sys.exit(1)

if __name__ == '__main__':
    main()

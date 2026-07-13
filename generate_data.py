#!/usr/bin/python3 -u
# -*- encoding: utf-8 -*-
'''
@File          :   generate_data.py
@LastModified  :   2026/07/13 15:00:00
@Author        :   ICer
@Contact       :   i_chip_backend@163.com
@WebSite       :   https://blog.csdn.net/i_chip_backend
@License       :   (C)Copyright 2018-2026, ICerDev
@Description   :   从 CDN 抓取 500 常用字笔画数据，生成 char-data-inline.js
'''

import urllib.request
import urllib.parse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

TOP500 = (
    '一了又力人儿几入八九十二七厂个么及千上小口山下与三万大于工才干土子也习已己马飞之义门广不无专天太开切王比五元车区支历中见日少内水为心方文六计认火斗以书办引队从今手分什化长公气月风反片毛他们代生用外处白务包出对发民加边可去本术正打东世平布示石龙节只叫号史由电业且四目北头主立它必记议市半写在地场有过达而成老动再机权西列划至存式百压她好如那阶红约级收观导会众自后向名合各多行年全先件任传价色华争同此当回因团光则并问关次安设许论产交决军农江米我近条你作但何住位体低身系利每角这没间应快完社识证况究状还进连运来极两严把报技声走却更花求形克志劳时里听员别步县即张改际局层的制和命周知所使例受往物金委备采质到事其现规者表林构直取或转拉青矿国图具明易些果非法治油定实学话该性放变育空单京府经组线细织建始参是省点思战界品响说前将总亲度美活济派类音养要相面带指持按政南型标查研革看种科信便保很律重选适复须段给结统院除家容部高被海流消调离资准效料能通难展验起都样根格真速原素热较造特候值铁般称积党圆着情清深断商率族眼常得做第象领理接据教基维道就装温然等程集画最量提斯期确联越强属想感意数新满解路照置群算管精需酸题影增器整'
)

URL_TPL = 'https://unpkg.com/hanzi-writer-data@2.0.1/{}.json'
OUTPUT = 'char-data-inline.js'
WORKERS = 20

HEADER = '''/*
 * @File          :   char-data-inline.js
 * @LastModified  :   2026/07/13 15:00:00
 * @Author        :   ICer
 * @Contact       :   i_chip_backend@163.com
 * @WebSite       :   https://blog.csdn.net/i_chip_backend
 * @License       :   (C)Copyright 2018-2026, ICerDev
 * @Description   :   汉字笔画数据（500 常用字），来自 hanzi-writer-data
 */

'''

HEADER_BRIEF = '''var CHAR_DATA = '''


def fetch_one(char):
    url = URL_TPL.format(urllib.parse.quote(char))
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=15) as resp:
                return char, json.loads(resp.read().decode('utf-8'))
        except Exception as e:
            if attempt < 2:
                time.sleep(0.5)
    return char, None


def main():
    total = len(TOP500)
    results = {}
    failures = []

    print(f'Fetching {total} characters ({WORKERS} concurrent)...')
    done = 0

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {pool.submit(fetch_one, c): c for c in TOP500}
        for f in as_completed(futures):
            char, data = f.result()
            done += 1
            sys.stdout.write(f'\r  [{done:3d}/{total}] {char}  ')
            sys.stdout.flush()
            if data:
                results[char] = data
            else:
                failures.append(char)

    print(f'\nDone. Success: {len(results)}, Failed: {len(failures)}')

    body = HEADER_BRIEF + json.dumps(results, ensure_ascii=False, separators=(',', ':'))

    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(HEADER)
        f.write(body)
        f.write('\n')

    size_kb = len(body.encode('utf-8')) / 1024
    print(f'Written to {OUTPUT} ({size_kb:.1f} KB)')

    if failures:
        print(f'Skipped {len(failures)} chars: {"".join(failures)}', file=sys.stderr)


if __name__ == '__main__':
    main()

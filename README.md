<!--
  @File          :   README.md
  @LastModified  :   2026/07/13 10:30:00
  @Author        :   ICer
  @Contact       :   i_chip_backend@163.com
  @WebSite       :   https://blog.csdn.net/i_chip_backend
  @License       :   (C)Copyright 2018-2026, ICerDev
  @Description   :   项目说明文档
-->

# 汉字笔画演示

输入汉字或句子，逐字播放标准笔画顺序动画。

## 使用方法

### Windows

双击 `start.bat` 启动本地服务器，浏览器自动打开。

### 其他系统

```bash
python -m http.server 8899
```

然后访问 http://localhost:8899/

### 环境要求

- Python 3（内置 http.server，无需额外安装）

## 文件说明

| 文件 | 说明 |
|---|---|
| `index.html` | 主页面 |
| `hanzi-writer.min.js` | 笔画渲染引擎 |
| `char-data-inline.js` | 汉字笔画数据（15 个常用字） |
| `start.bat` | Windows 一键启动脚本 |

## 功能

- 输入单字或整句话，自动提取汉字并逐个播放
- 暂停/继续/循环控制
- 示例字快捷查看
- 支持部首高亮

## 许可证

本项目代码（index.html、start.bat、README.md）采用 **MIT 协议**，详见 `LICENSE`。

### 第三方组件

| 组件 | 协议 | 许可文件 |
|---|---|---|
| [hanzi-writer](https://github.com/chanind/hanzi-writer) | MIT | `LICENSE.hanzi-writer` |
| [hanzi-writer-data](https://github.com/chanind/hanzi-writer-data) | Arphic Public License | `ARPHICPL.TXT` |
| 笔画数据来源：[Make Me a Hanzi](https://github.com/skishore/makemeahanzi) | Arphic Public License | 同上 |

---
icon: lucide/rocket
---

# 开始使用

完整文档请访问 [zensical.org](https://zensical.org/docs/)。

## 命令

* [`zensical new`][new] - 创建新项目
* [`zensical serve`][serve] - 启动本地Web服务器
* [`zensical build`][build] - 构建您的站点

  [new]: https://zensical.org/docs/usage/new/
  [serve]: https://zensical.org/docs/usage/preview/
  [build]: https://zensical.org/docs/usage/build/

## 示例

### 注释框

> 前往 [文档](https://zensical.org/docs/authoring/admonitions/)

!!! note

    这是一个 **note** 注释框。用于提供有用的信息。

!!! warning

    这是一个 **warning** 注释框。请注意！

### 详细信息

> 前往 [文档](https://zensical.org/docs/authoring/admonitions/#collapsible-blocks)

??? info "点击展开更多信息"
    
    此内容在您点击展开前是隐藏的。
    非常适合常见问题解答或长篇解释。

## 代码块

> 前往 [文档](https://zensical.org/docs/authoring/code-blocks/)

``` python hl_lines="2" title="代码块"
def greet(name):
    print(f"Hello, {name}!") # (1)!

greet("Python")
```

1.  > 前往 [文档](https://zensical.org/docs/authoring/code-blocks/#code-annotations)

    代码注释允许为代码行附加注释。

代码也可以内联高亮： `#!python print("Hello, Python!")`。

## 内容标签

> 前往 [文档](https://zensical.org/docs/authoring/content-tabs/)

=== "Python"

    ``` python
    print("Hello from Python!")
    ```

=== "Rust"

    ``` rs
    println!("Hello from Rust!");
    ```

## 图表

> 前往 [文档](https://zensical.org/docs/authoring/diagrams/)

``` mermaid
graph LR
  A[开始] --> B{错误？};
  B -->|是| C[嗯...];
  C --> D[调试];
  D --> B;
  B ---->|否| E[好！];
```

## 脚注

> 前往 [文档](https://zensical.org/docs/authoring/footnotes/)

这里是一个带有脚注的句子。[^1]

悬停查看工具提示。

[^1]: 这是脚注。


## 格式化

> 前往 [文档](https://zensical.org/docs/authoring/formatting/)

- ==这是标记（高亮）==
- ^^这是插入（下划线）^^
- ~~这是删除（删除线）~~
- H~2~O
- A^T^A
- ++ctrl+alt+del++

## 图标、表情符号

> 前往 [文档](https://zensical.org/docs/authoring/icons-emojis/)

* :sparkles: `:sparkles:`
* :rocket: `:rocket:`
* :tada: `:tada:`
* :memo: `:memo:`
* :eyes: `:eyes:`

## 数学公式

> 前往 [文档](https://zensical.org/docs/authoring/math/)

$$
\cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}
$$

!!! warning "需要配置"
    请注意，MathJax 是通过此页面上的 `script` 标签包含的，并且在生成的默认配置中没有配置，以避免将其包含在不需要它的页面中。有关如何在所有页面上配置它的详细信息，请参阅文档，如果您的页面比这些简单入门页面包含更多的数学内容。

<script id="MathJax-script" async src="https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js"></script>
<script>
  window.MathJax = {
    tex: {
      inlineMath: [["\\(", "\\)"]],
      displayMath: [["\\[", "\\]"]],
      processEscapes: true,
      processEnvironments: true
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    }
  };
</script>

## 任务列表

> 前往 [文档](https://zensical.org/docs/authoring/lists/#using-task-lists)

* [x] 安装 Zensical
* [x] 配置 `zensical.toml`
* [x] 编写出色的文档
* [ ] 部署到任何地方

## 工具提示

> 前往 [文档](https://zensical.org/docs/authoring/tooltips/)

[悬停查看][example]

  [example]: https://example.com "我是工具提示！"

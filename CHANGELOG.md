# [0.3.7] 23-02-14

- 修改： ExecuteResult 支持获得 Popen 的对象。

# [0.3.6] 23-01-12

- 修改：提供 Executor exit_hook 参数，能够自定义程序执行出错的退出流程。
- 移除： 在 execute_straight finish 时输出空行的逻辑。

# [0.3.5] 23-01-10

- 修改： 在 execute_straight finish 时输出一个空行。
- 修复： load_unity_path_config config_yaml.keys() subscriptable error.

# [0.3.4] 23-01-04

- 修改：replace simplelogger with python logging module；
- 移除： simplelogger.LOG_INDENT 等常量值。

# [0.3.3] 22-12-30

- 修复：simplelogger 钩子函数在外部使用时无效的问题。

# [0.3.2] 22-12-29

- 修复： yaml.load 替换为 yaml.safe_load。
- 新增： simplelogger 添加 hook_info、hook_warning、hook_error 以及相关测试用例。

# [0.3.1] 22-12-28

- 修复： get_unity_path None error.

# [0.3.0] 22-12-28

- 修改：导出的包不再包含 test 内容。
- 修复： execute_straight 当 shell 为 True 时，windows 使用双斜杠路径会导致执行失败，解决办法为当 shell 为 True 时，对 cmd 先做一次 normpath。
- 新增： executor 添加 get_unity_path 函数。

# [0.2.16] 22-12-22

- 修复：executor 解决 shell 为 False 的情况下如果包装了 cmd 在 windows 上会出现 ‘PermissionError: [WinError 5] 拒绝访问。’ 的问题。

# [0.2.15] 22-12-21

- 修复：sync_folder 删除 symlink 文件夹失败的问题。
- 修复：sync_folder 清理相对目录不对的文件时，按不区分大小写的文件系统规则处理路径。
- 修改：Popen shell 为 True 时使用 str 作为 args，否则使用 list 作为 args。

# [0.2.14] 22-12-06

- 修改：Popen 的 process.communicate() 包装为 Thread ，以接收来自用户的中断信号。

# [0.2.13] 22-12-02

- 修复：urllib 绕过 MacOS 的 CA 问题。

# [0.2.12] 22-11-30


- 修复：sync_folder 使用 remove_empty_dirs 函数修复不正确的逻辑。
- 修改：Executor 输出详情时带上 WorkDir。

# [0.2.11] 22-11-24

- 修改：sync_folder 对于 files_to_sync 获取绝对路径时会修改工作目录到 src_parent_path。

# [0.2.10] 22-11-24

- 新增：fsext sync_folder 和 get_dirs 函数。
- 新增：execute_straight 添加能够 hook 到 process 的 callback。
- 新增：format_args 函数改为 public。

# [0.2.9] 22-11-14

- 修复：修正 detect_encoding 的警告提醒。
- 新增：windows 下可以使用 execute_by_cmd 来使用 cmd 执行命令。
- 新增：shorthand 新增 is_admin_win 判断是否处在 windows 管理员模式下。
- 修改：log 的 level 不为 LOG_LEVEL_ERROR 时，输出到 stdout。
- 修改：copy_files 对于目标文件夹已存在的情况，先删除目标文件夹再调用 shutil.copytree。

# [0.2.8] 22-09-19

- 修复： wrap_blank_with_double_quotes 参数不会错误的包装已经有双引号的内容。

# [0.2.7] 22-09-07

- 新增： convert_encoding 猜测当前的文件编码并将其转为一个指定的编码。
- 修改： detect_encoding 从 executor 模块迁移到 fsext 模块内，旧函数已被标记为 deprecated。

# [0.2.6] 22-08-16

- 修复： execute_file 调用 execute_straight 参数错误的问题。
- 修改： execute_file 的 args 默认为 None ，且内部不做 __format_args 的处理，延迟到 execute_straight 再做。
- 修复： __ext2exe 的 .py 后缀对应可执行文件改为 sys.executable。

# [0.2.5] 22-08-16

- 修复：autoupgrade 的 upgrade 函数中 executor 启用 wrap_blank_with_double_quotes 参数。

# [0.2.4] 22-08-16

- 新增： executor.py 添加参数 wrap_blank_with_double_quotes ， 将含有空白字符的内容（命令、参数）用双引号包装。

# [0.2.3] 22-08-12

- 修复： install_requires 为空的情况

# [0.2.2] 22-08-02

- 修复：python 3.10+ 才支持 orig_argv 参数。

# [0.2.1] 22-08-02

- 修复：autoupgrade 逻辑问题，并添加一些 log 信息。

# [0.2.0] 22-08-02

- 添加 autoupgrade 模块。

# [0.1.3] 22-07-12 

- 修改：fsext copy_files 使用 shutil.copytree
- 添加：fsext to_base64 将图片数据转为 base64 格式

# [0.1.2] 22-06-09

- 修复：executor 修改工作目录的参数放到最后，修复未定义字段的错误。

# [0.1.1] 22-06-09

- 添加：executor 修改工作目录的参数。

# [0.1.0] 22-06-01

- simplelogger ErrorRaiseExcpetion 使用模块内全局变量。
- 修复：executor set_env_win override 为 False 时，无效语法的错误。
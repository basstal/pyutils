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
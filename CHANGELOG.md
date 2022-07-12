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
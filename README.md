# fast_lio
看到你遇到了GitHub文件大小限制的问题。这个错误明确指出了问题所在：你尝试推送的 converted_ros2_bag.db3文件大小为 ​​913.83 MB​​，这远远超过了 GitHub 规定的 ​​100 MB​​ 单文件上限
。
神人报错，gitignore忽略了还会传bag
```
ros2 launch node_launch run.launch.py 
```
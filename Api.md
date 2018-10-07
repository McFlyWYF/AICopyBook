## Django操作

| 编号 | URL                                                          | 备注                     | 方法 |
| ---- | ------------------------------------------------------------ | ------------------------ | ---- |
| 1    | 39.105.110.19/media/media/图片名                             | 访问头像                 | GET  |
| 2    | 39.105.110.19/register/?account=?&password=?&age=?&avatar=?  | 注册(avatar参数可以为空) | POST |
| 3    | 39.105.110.19/login/?account=?&password=?                    | 登录                     | POST |
| 4    | 39.105.110.19/collect/?id=?&dir=?&user=?                     | 收藏                     | POST |
| 5    | 39.105.110.19/friend/?id=?&date=?&text=?&url=?&stick=?&likenum=?&sharenum=?&user=? | 朋友圈                   | POST |
| 6    | 39.105.110.19/copybookList/碑帖名                            | 碑帖图片                 | GET  |
| 7    | 39.105.110.19/copybookAll                                    | 所有碑帖图片(用不到)     | GET  |
| 8    | 39.105.110.19/WordsOutline                                   | 字体轮廓图               | GET  |
| 9    | 39.105.110.19/ChinesePainting                                | 国画                     | GET  |
| 10   | 39.105.110.19/findwords/?author=书法家名&word=字名           | 提取单独字               | GET  |
| 11   | 39.105.110.19/friends                                        | 获取朋友圈信息           | GET  |
| 12   | 39.105.110.19/myuser/用户名                                  | 每个用户的动态           | GET  |
| 13   | 39.105.110.19/collect                                        | 查看收藏品               | GET  |


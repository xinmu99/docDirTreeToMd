# docDirTreeToMd

create docment dir to docrify sidebar.md

文件目录树生成 markdown 目录导航  

应用于 docrify sidebar.md

- 文件类型过滤 说明

    `def filter_f_d(x): return x.split('.')[-1] not in {"py"}`   过滤函数，默认设置为 排除 py类型文件


  如果  仅仅给md文件做目录需要修改为：

  `def filter_f_d(x): return x.split('.')[-1] in {"md"}`

---
比如生成以下目录树 

- [1.1. 7plus.xml](/7plus.xml)
- [1.2. Accessor.xml](/Accessor.xml)
- [1.3. All Events.xml](/All Events.xml)
- [1.4. CMD.xml](/CMD.xml)
- [1.5. Context Menu.xml](/Context Menu.xml)
- [1.6. Explorer Buttons.xml](/Explorer Buttons.xml)
- [1.7. Explorer.xml](/Explorer.xml)
- [1.8. Fast Folders.xml](/Fast Folders.xml)
- [1.9. File Dialog.xml](/File Dialog.xml)
- [1.10. Internet.xml](/Internet.xml)
- [1.11. Misc Hotkeys.xml](/Misc Hotkeys.xml)
- [1.12. Numpad Enhancements.xml](/Numpad Enhancements.xml)
- [1.13. Old Versions](/Old Versions)
    - [1.13.1. 2.3.0](/Old Versions\2.3.0)
        - [1.13.1.1. All Events.xml](/Old Versions\2.3.0\All Events.xml)
    - [1.13.2. 2.4.0](/Old Versions\2.4.0)
        - [1.13.2.1. All Events.xml](/Old Versions\2.4.0\All Events.xml)
    - [1.13.3. 2.5.0](/Old Versions\2.5.0)
        - [1.13.3.1. All Events.xml](/Old Versions\2.5.0\All Events.xml)
- [1.14. Taskbar.xml](/Taskbar.xml)
- [1.15. Window Handling.xml](/Window Handling.xml)



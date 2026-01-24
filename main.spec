# -*- mode: python ; coding: utf-8 -*-

datas=[
    ("src/conf","conf"),
    ("src/my_sdk","my_sdk"),
    ("src/biz","biz"),
    ("alembic","alembic"),
    ("alembic.ini","."),
]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[
        "typer", "click", "ctypes", "_ctypes",
        "colorlog",
        'scipy', 'scipy._cyutility',
        "alembic",
        'sqlalchemy', 'sqlmodel', "sqlalchemy.sql.default_comparator",
        "sqlalchemy.engine.url", "sqlalchemy.dialects.sqlite",
        'sqlite3',
        "uvicorn.logging",          # 核心日志模块
        "uvicorn.logging.DefaultFormatter",  # 显式指定默认格式化器
        "logging.config",           # Python 标准库日志配置
        "colorama",                  # 若使用颜色日志，需添加（Uvicorn 可能依赖）
        "uvicorn.loops",
        "uvicorn.loops.auto",
        "uvicorn.protocols",
        "uvicorn.protocols.http",
        "uvicorn.protocols.http.auto",
        "uvicorn.protocols.websockets",
        "uvicorn.protocols.websockets.auto",
        "uvicorn.lifespan",
        "uvicorn.lifespan.on",
        "fastapi.middleware.cors"
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

onefile=False
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=not onefile,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
if not onefile:
    coll = COLLECT(
        exe,
        a.binaries,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name='main',
    )

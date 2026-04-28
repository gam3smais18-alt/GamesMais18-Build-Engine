# =============================================================================
# 🛸 GAMES MAIS 18 - PROJETO OVERLORD V3.0 (ULTIMATE INTERCEPTOR)
# =============================================================================
# Engenharia de Elite: Redirecionamento Total, Injeção de Patches e Auto-Index
# =============================================================================

python early:
    import os
    import shutil

    # --- [ CONFIGURAÇÃO DE ALVO ] ---
    G18_ID = "gm18.grandmashouse"
    RAIZ_NOME = "GamesMais18"

    # --- [ LOCALIZADOR DE COORDENADAS ] ---
    if renpy.android:
        # Busca o caminho real do SDCard/Armazenamento Interno
        try:
            from jnius import autoclass
            Environment = autoclass('android.os.Environment')
            base_path = Environment.getExternalStorageDirectory().getAbsolutePath()
        except:
            base_path = "/storage/emulated/0"

        caminho_g18 = os.path.join(base_path, RAIZ_NOME, G18_ID)
    else:
        # PC: Cria uma célula portátil de saves
        caminho_g18 = os.path.join(config.basedir, "G18_Mothership", G18_ID)

    # --- [ PROTOCOLO DE CONSTRUÇÃO DE BASE ] ---
    # Criamos a hierarquia de pastas se ela não existir
    for subfolder in ["", "patches", "archives", "saves"]:
        target = os.path.join(caminho_g18, subfolder)
        if not os.path.exists(target):
            try:
                os.makedirs(target)
            except:
                pass

    # =========================================================================
    # 🛰️ MÓDULO DE INTERCEPTAÇÃO (INJEÇÃO DE PRIORIDADE)
    # =========================================================================
    # Diferencial G18: Usamos 'insert(0)' para que os arquivos externos
    # substituam os arquivos originais do APK (Patches dinâmicos).

    if os.path.exists(caminho_g18):
        # 1. Pasta de Patches (Imagens/Sons soltos) - PRIORIDADE MÁXIMA
        patch_dir = os.path.join(caminho_g18, "patches")
        config.searchpath.insert(0, patch_dir)

        # 2. Pasta de Archives (.rpa externos)
        arch_dir = os.path.join(caminho_g18, "archives")
        config.searchpath.insert(1, arch_dir)
        config.searchpath.insert(2, caminho_g18)

        # 3. AUTO-INDEXER DE RPA (Engenharia de Ponta)
        # Registra automaticamente qualquer .rpa colocado pelo usuário
        def scan_and_mount(directory):
            try:
                for f in os.listdir(directory):
                    if f.endswith(".rpa"):
                        label = f.replace(".rpa", "")
                        if label not in config.archives:
                            config.archives.append(label)
            except:
                pass

        scan_and_mount(caminho_g18)
        scan_and_mount(arch_dir)

    # =========================================================================
    # 💾 MÓDULO DE PERSISTÊNCIA (SAVES & RADAR VIP)
    # =========================================================================
    save_final_path = os.path.join(caminho_g18, "saves")

    # Redireciona o diretório de salvamento oficial
    config.save_directory = G18_ID
    config.savedir = save_final_path

    # Protocolo de Migração Automática de Saves de Versões Antigas
    def migrar_saves():
        try:
            # Localiza a pasta "morta" (padrão do Android)
            old_dir = renpy.loader.get_path(G18_ID)
            if os.path.exists(old_dir) and old_dir != save_final_path:
                for f in os.listdir(old_dir):
                    src = os.path.join(old_dir, f)
                    dst = os.path.join(save_final_path, f)
                    if os.path.isfile(src) and not os.path.exists(dst):
                        shutil.copy2(src, dst)
        except:
            pass

    migrar_saves()

    # --- [ OTIMIZAÇÃO DE BUSCA ] ---
    # Limita o cache para não travar o celular ao ler arquivos externos grandes
    config.image_cache_size = 32 if renpy.android else 64

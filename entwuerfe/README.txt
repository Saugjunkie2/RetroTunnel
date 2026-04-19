================================================================================
ENTWUERFE — PUFFER-ORDNER (Root-Level)
================================================================================
STATUS: PUFFER
DATUM: 2026-04-19

ZWECK:
  Dieser Root-Ordner dient als Puffer fuer Entwuerfe die noch
  keinem Base- oder Modul-Ordner zugeordnet sind. Sobald ein
  Thema einem Base/Mod zugeordnet werden kann, wird der Entwurf
  in den entwuerfe/-Unterordner der jeweiligen Base verschoben.

NEUE STRUKTUR (ab 2026-04-19):
  Entwuerfe leben in entwuerfe/-Unterordnern innerhalb der
  zugehoerigen Base- oder Modul-Ordner. Beispiel:
    base/BASE-050_FIREWALL_CORE/entwuerfe/portfreigaben/

BEREITS VERSCHOBEN:
  identity_schema/        → BASE-010_IDENTITY_CORE/entwuerfe/
  boot-firewall-baseline/ → BASE-050_FIREWALL_CORE/entwuerfe/
  portfreigaben/          → BASE-050_FIREWALL_CORE/entwuerfe/
  admin-dashboard/        → BASE-110_WEBSTACK_CORE/entwuerfe/
  panel-zentrale/         → BASE-110_WEBSTACK_CORE/entwuerfe/
  psk-secret-lifecycle/   → BASE-110_WEBSTACK_CORE/entwuerfe/

GOVERNANCE: KR-01 (00_MANIFEST.txt §7).
  Alle entwuerfe/-Ordner sind NICHT normativ.
  Keine Einflussnahme auf das Konzept.
  Verweise muessen mit (KR-01) markiert sein.

HINWEIS: Leere Ordner-Huellen der verschobenen Themen koennen
manuell geloescht werden (Marco).
================================================================================

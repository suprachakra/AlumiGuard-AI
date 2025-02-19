```mermaid
graph LR
    A[Primary Region] -- Replication --> B[Secondary Region]
    A -- Failover Trigger --> B
    B -- Active Backup --> A
    C[Global Users] --> A
    C --> B
```

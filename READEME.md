# Ambiente Docker Compose

## Subir os serviços

```bash
docker compose up -d
```

---

## Ver logs

```bash
docker compose logs -f
```

---

## Parar os containers

```bash
docker compose down
```

---

## Executar profile Adminer

```bash
docker compose --profile tools up -d
```

Acesse:

http://localhost:8080

---

## Limpar completamente o ambiente

```bash
docker compose down -v
```

Este comando remove:

- containers
- rede
- volume do PostgreSQL

---

## Estrutura

- web → aplicação Python
- db → PostgreSQL
- adminer → interface web do banco
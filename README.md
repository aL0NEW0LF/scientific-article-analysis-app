# Getting started
## Without docker

**Backend**

```shell
cd scientific-article-analysis-app
```

```shell
cd apps/api
```

**Windows**

```shell
py -3 -m venv .venv
```

**MacOS/Linus**

```shell
python3 -m venv .venv
```

Then, activate the env:

**Windows**

```shell
.venv\Scripts\activate
```

**MacOS/Linus**

```shell
. .venv/bin/activate
```

You can run the following command to install the dependencies:

```shell
pip3 install -r requirements.txt
```

Then you are good to go.

Start the server with:

```shell
langchain serve
```

**Frontend**

```shell
cd scientific-article-analysis-app
```

```shell
cd apps/chat-ui
```

```shell
npm install
```

```shell
npm run dev -- --open
```

**Storage**

Use mongo atlas or a local mongodb andd plug it in the .env file.

## With docker

```shell
cd scientific-article-analysis-app
```

```shell
docker compose -f docker-compose.yml up -d
```

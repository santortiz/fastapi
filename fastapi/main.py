import uvicorn


if __name__== "__main__":
    print("API running!")
    uvicorn.run("app.app:app", port=8000, reload=True)

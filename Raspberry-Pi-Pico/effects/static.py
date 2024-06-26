from lib.Effect import Effect

def callback(ledstrip, color):
    ledstrip.fill(color)

static: Effect = Effect("static", callback)

    
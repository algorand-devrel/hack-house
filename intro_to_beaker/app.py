from beaker import *
from pyteal import *

class ApplicationState:
    counter = GlobalStateValue(stack_type=TealType.uint64)

app = Application("HelloWorld", state=ApplicationState)

@app.external
def hello(name: abi.String, *, output: abi.String) -> Expr:
    return output.set(Concat(Bytes("Hello, "), name.get()))

@app.external
def add(a: abi.Uint64, b: abi.Uint64, *, output: abi.Uint64):
    return output.set(a.get() + b.get())

@app.external
def multi_logger(a: abi.String, b: abi.String, *, output: abi.String):
    return Seq(
        Log(a.get()),
        Log(b.get()),
        output.set(Concat(a.get(), b.get()))
    )

@app.external
def if_expression(input: abi.Uint64, *, output: abi.String):
    return If(
        input.get() > Int(5), 
        output.set(Bytes("Input is greater than five")),
        output.set(Bytes("Input is NOT greater than five"))
    )

@app.external
def if_else_if(input: abi.Uint64, *, output: abi.String):            
    return If(
        input.get() > Int(5)
    ).Then(
        output.set(Bytes("Input is greater than five"))
    ).ElseIf(
        input.get() == Int(5)
    ).Then(
        output.set(Bytes("Input IS five"))
    ).Else(
        output.set(Bytes("Input is NOT greater than five"))
    )

@app.external
def cond_expression(input: abi.Uint64, *, output: abi.String):
    return Cond(
        [input.get() == Int(1), output.set(Bytes("The value was one!"))],
        [input.get() == Int(2), output.set(Bytes("The value was two!"))]
        # Fail if neither is true
    )

@app.external
def increment(amount: abi.Uint64, *, output: abi.Uint64 ):
    return Seq(
        app.state.counter.set(app.state.counter + amount.get()),
        output.set(app.state.counter.get())
    )

@app.delete(authorize=Authorize.only(Global.creator_address()))
def delete() -> Expr:
    return Approve()

app.build().export("./artifacts")

accounts = sandbox.kmd.get_accounts()
sender = accounts[0]

app_client = client.ApplicationClient(
    client=sandbox.get_algod_client(),
    app=app,
    sender=sender.address,
    signer=sender.signer,
)

app_client.create()
return_value = app_client.call(hello, name="Beaker").return_value
print(return_value)

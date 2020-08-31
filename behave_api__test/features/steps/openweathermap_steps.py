import requests

from behave import given, when, then
from features.api.openweathermap import OpenWeatherMap

@given(u'que sou usuário')
def step_impl(context):
    context.api = OpenWeatherMap(context.config.userdata)

@when(u'eu requisitar a previsao do tempo da através do "{ID}" da cidade')
def step_impl(context, ID: str):
    context.response: Response = context.api.day_temperature(int(ID))
    
@then(u'o serviço deve retornar a "{cidade}" consultada')
def step_impl(context, cidade: str):
    context.response = context.response.json()
    assert(context.response["city"]["name"]) == cidade

@then(u'o serviço deve retornar status code "{code}"')
def step_impl(context, code: str):
    assert (context.response.status_code == int(code))

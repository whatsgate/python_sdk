# swagger_client.DefaultApi

All URIs are relative to *https://whatsgate.ru/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_post**](DefaultApi.md#check_post) | **POST** /check | Проверка зарегистрирован ли номер в WhatsApp
[**get_chats_post**](DefaultApi.md#get_chats_post) | **POST** /get-chats | Возвращает список активных чатов
[**seen_post**](DefaultApi.md#seen_post) | **POST** /seen | Отправляет команду в чат, что последние сообщения просмотрены
[**send_message**](DefaultApi.md#send_message) | **POST** /send | Отправка сообщения

# **check_post**
> InlineResponse2001 check_post(body)

Проверка зарегистрирован ли номер в WhatsApp

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.CheckBody() # CheckBody | Проверяет, зарегистрирован ли указанный номер в WhatsApp. Номер указывается в формате только цифр, например 79999999999

try:
    # Проверка зарегистрирован ли номер в WhatsApp
    api_response = api_instance.check_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->check_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CheckBody**](CheckBody.md)| Проверяет, зарегистрирован ли указанный номер в WhatsApp. Номер указывается в формате только цифр, например 79999999999 | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chats_post**
> InlineResponse2002 get_chats_post(body)

Возвращает список активных чатов

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.GetchatsBody() # GetchatsBody | Запрашивает и возвращает список активных чатов, включая контакты и группы. В объекте группы находится идентификатор группы, список всех участников группы, права участников (является ли участник администратором группы).

try:
    # Возвращает список активных чатов
    api_response = api_instance.get_chats_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_chats_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetchatsBody**](GetchatsBody.md)| Запрашивает и возвращает список активных чатов, включая контакты и группы. В объекте группы находится идентификатор группы, список всех участников группы, права участников (является ли участник администратором группы). | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seen_post**
> InlineResponse2004 seen_post(body)

Отправляет команду в чат, что последние сообщения просмотрены

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.SeenBody() # SeenBody | Команда устанавливает у всех сообщений в указанном чате статус просмотрены.

try:
    # Отправляет команду в чат, что последние сообщения просмотрены
    api_response = api_instance.seen_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->seen_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SeenBody**](SeenBody.md)| Команда устанавливает у всех сообщений в указанном чате статус просмотрены. | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message**
> InlineResponse200 send_message(body)

Отправка сообщения

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.SendBody() # SendBody | Отправляет текстовое или мультимедийное сообщение контакту либо группе. Может использоваться синхронно (возвращает ответ после отправки сообщения, ответ содержит объект отправленного сообщения с идентификатором), либо асинхронно (ответ содержит результат постановки в очередь, а отправленное сообщение приходит на указанный webhook). По умолчанию используется асинхронная отправка.

try:
    # Отправка сообщения
    api_response = api_instance.send_message(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->send_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SendBody**](SendBody.md)| Отправляет текстовое или мультимедийное сообщение контакту либо группе. Может использоваться синхронно (возвращает ответ после отправки сообщения, ответ содержит объект отправленного сообщения с идентификатором), либо асинхронно (ответ содержит результат постановки в очередь, а отправленное сообщение приходит на указанный webhook). По умолчанию используется асинхронная отправка. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


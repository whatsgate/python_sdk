# swagger_client._Api

All URIs are relative to *https://whatsgate.ru/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_media_post**](_Api.md#get_media_post) | **POST** /get-media | Возвращает объект медиафайла, прикрепленного к сообщению

# **get_media_post**
> InlineResponse2003 get_media_post(body)

Возвращает объект медиафайла, прикрепленного к сообщению

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
api_instance = swagger_client._Api(swagger_client.ApiClient(configuration))
body = swagger_client.GetmediaBody() # GetmediaBody | Запрашивает и возвращает медиа-файл, прикрепленный к сообщению по идентификатору mediaKey.

try:
    # Возвращает объект медиафайла, прикрепленного к сообщению
    api_response = api_instance.get_media_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling _Api->get_media_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetmediaBody**](GetmediaBody.md)| Запрашивает и возвращает медиа-файл, прикрепленный к сообщению по идентификатору mediaKey. | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


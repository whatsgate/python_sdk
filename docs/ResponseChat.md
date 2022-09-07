# ResponseChat

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор контакта или группы в формате WhatsApp | [optional] 
**name** | **str** | Имя контакта или группы | [optional] 
**is_group** | **bool** | Является ли чат контактом или группой | [optional] 
**is_read_only** | **bool** | Является ли чат ReadOnly | [optional] 
**unread_count** | **int** | Количество непрочитанных сообщений в чате | [optional] 
**timestamp** | **int** | Время последней активночти в чате | [optional] 
**pinned** | **bool** | Является ли чат закрепленным | [optional] 
**is_muted** | **bool** | Выключен ли у чата звук | [optional] 
**mute_expiration** | **bool** | Время, оставшееся до включения звука | [optional] 
**group_metadata** | [**ResponseChatGroupMetadata**](ResponseChatGroupMetadata.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


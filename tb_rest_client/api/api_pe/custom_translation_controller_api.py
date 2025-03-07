# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.3.3PAAS-RC1
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class CustomTranslationControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_current_custom_translation_using_get(self, **kwargs):  # noqa: E501
        """Get Custom Translation configuration (getCurrentCustomTranslation)  # noqa: E501

        Fetch the Custom Translation map that corresponds to the authority of the user. The API call is designed to load the custom translation items for edition. So, the result is NOT merged with the parent level configuration. Let's assume there is a custom translation configured on a system level. And there is no custom translation items configured on a tenant level. In such a case, the API call will return empty object for the tenant administrator.    Response example:   ```json {\"translationMap\":{\"es_ES\":\"{\\\"home\\\":\\\"MyHome\\\"}\"}} ```  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_custom_translation_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CustomTranslation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_current_custom_translation_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_current_custom_translation_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_current_custom_translation_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Custom Translation configuration (getCurrentCustomTranslation)  # noqa: E501

        Fetch the Custom Translation map that corresponds to the authority of the user. The API call is designed to load the custom translation items for edition. So, the result is NOT merged with the parent level configuration. Let's assume there is a custom translation configured on a system level. And there is no custom translation items configured on a tenant level. In such a case, the API call will return empty object for the tenant administrator.    Response example:   ```json {\"translationMap\":{\"es_ES\":\"{\\\"home\\\":\\\"MyHome\\\"}\"}} ```  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_custom_translation_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CustomTranslation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_current_custom_translation_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/customTranslation/currentCustomTranslation', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomTranslation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_custom_translation_using_get(self, **kwargs):  # noqa: E501
        """Get end-user Custom Translation configuration (getCustomTranslation)  # noqa: E501

        Fetch the Custom Translation map for the end user. The custom translation is configured in the white labeling parameters. If custom translation translation is defined on the tenant level, it overrides the custom translation of the system level. Similar, if the custom translation is defined on the customer level, it overrides the translation configuration of the tenant level.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_translation_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CustomTranslation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_custom_translation_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_custom_translation_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_custom_translation_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get end-user Custom Translation configuration (getCustomTranslation)  # noqa: E501

        Fetch the Custom Translation map for the end user. The custom translation is configured in the white labeling parameters. If custom translation translation is defined on the tenant level, it overrides the custom translation of the system level. Similar, if the custom translation is defined on the customer level, it overrides the translation configuration of the tenant level.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_translation_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CustomTranslation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_custom_translation_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/customTranslation/customTranslation', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomTranslation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_custom_translation_using_post(self, **kwargs):  # noqa: E501
        """Create Or Update Custom Translation (saveCustomTranslation)  # noqa: E501

        Creates or Updates the Custom Translation map.   Request example:   ```json {\"translationMap\":{\"es_ES\":\"{\\\"home\\\":\\\"MyHome\\\"}\"}} ```  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_custom_translation_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomTranslation body:
        :return: CustomTranslation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_custom_translation_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.save_custom_translation_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def save_custom_translation_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create Or Update Custom Translation (saveCustomTranslation)  # noqa: E501

        Creates or Updates the Custom Translation map.   Request example:   ```json {\"translationMap\":{\"es_ES\":\"{\\\"home\\\":\\\"MyHome\\\"}\"}} ```  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_custom_translation_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomTranslation body:
        :return: CustomTranslation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_custom_translation_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/customTranslation/customTranslation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomTranslation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

/* Copyright 2020 Intel Corporation
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/

#include <stdlib.h>

#include "types.h"
#include "ext_work_order_info.h"

// ExtWorkOrderInfoImpl class implements ExtWorkOrderInfo interface
class ExtWorkOrderInfoImpl : public ExtWorkOrderInfo {
public:
    ExtWorkOrderInfoImpl();

    ~ExtWorkOrderInfoImpl();

    /* Parameters:
           data [OUT] - workorder extended data (if present) or it is not used
       Returns:
           size of the workorder extra data or null if none is provided
    */
    virtual size_t GetWorkOrderExData(ByteArray& data) override;

    /* Verifies an attestation info and returns its MRENCLAVE,
       MRSIGNER, Encryption Key, Verification Key on success.
     Parameters:
        attestation_data - attestation to verify
        mrenclave [OUT] - MRENCLAVE value from the attestation_data
                          on success or not used
        mrsigner [OUT] - MRSIGNER value from the attestation_data
                         on success or not used
        encryption_pub_key [OUT] - public encryption key from the
                                   attestation_data on success or not used
        verification_key [OUT] - public verification key from the
                                 attestation_data on success or not used
     Returns:
        zero on success or an error code otherwise
    */
    virtual int VerifyAttestation(const ByteArray& att_info, 
        ByteArray& mrenclave, 
        ByteArray& mrsigner, 
        ByteArray& verification_key, 
        ByteArray& encryption_pub_key) override;

    /*  Returns workorder request signing data, needed for cross-TEE processing.
        Parameters:
            verification_key [OUT] - requester key used to sign the workorder
            requester_nonce [OUT] - nonce provided by the workorder requester
                                    as part of the signature 
            reserved_worker_nonce [OUT] - reserved for future to hold nonce
                                    provided by the worker for this workorder
        Returns:
            true if the workorder was signed or false otherwise
    */
    virtual bool GetWorkorderSigningInfo(ByteArray& verification_key,
        ByteArray& requester_nonce,
        ByteArray& reserved_worker_nonce) override;

};  // ExtWorkOrderInfo

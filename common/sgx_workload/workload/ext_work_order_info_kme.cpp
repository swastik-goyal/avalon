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

#include "crypto.h"
#include "utils.h"
#include "hex_string.h"
#include "types.h"
#include"error.h"

#include "enclave_utils.h"
#include "ext_work_order_info_kme.h"

ExtWorkOrderInfoKME::ExtWorkOrderInfoKME() {}

ExtWorkOrderInfoKME::~ExtWorkOrderInfoKME() {}

int ExtWorkOrderInfoKME::GenerateSigningKey(
    KeyType type, const ByteArray& nonce_hex,
    ByteArray& signing_key, ByteArray& verification_key_hex,
    ByteArray& verification_key_signature_hex) {

    // To be implemented
    return TCF_SUCCESS;
}  // ExtWorkOrderInfoKME::GenerateSigningKey

int ExtWorkOrderInfoKME::VerifyAttestaionWpe(
    const ByteArray& attestation_data, const ByteArray& hex_id,
    ByteArray& mrenclave, ByteArray& mrsigner,
    ByteArray& encryption_public_key, ByteArray& verification_key_hex) {

    // To be implemented
    return 0;
}  // ExtWorkOrderInfoKME::VerifyAttestaionWpe

int ExtWorkOrderInfoKME::CreateWorkorderKeyInfo(const ByteArray& wpe_key,
    const ByteArray& kme_skey, ByteArray& json_key_data) {

    // To be implemented
    return 0;
}  // ExtWorkOrderInfoKME::CreateWorkorderKeyInfo

bool ExtWorkOrderInfoKME::CheckAttestationSelf(
    const ByteArray& attestation_data, ByteArray& mrenclave,
    ByteArray& mrsigner, ByteArray& verivication_key,
    ByteArray& encryption_public_key) {

    // To be implemented
    return 0;
}  // ExtWorkOrderInfoKME::CheckAttestationSelf

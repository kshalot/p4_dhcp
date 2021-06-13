#include <core.p4>
#include <v1model.p4>

#include "header.p4"
#include "parser.p4"

control egress(inout headers hdr, inout metadata meta, inout standard_metadata_t standard_metadata) {
    apply { }
}

control ingress(inout headers hdr, inout metadata meta, inout standard_metadata_t standard_metadata) {
    action _drop() {
        // mark_to_drop(standard_metadata);
        standard_metadata.egress_spec = 1;
    }
    action set_dport(bit<9> port) {
        standard_metadata.egress_spec = port;
    }
    table forward_l2 {
        actions = {
            set_dport;
            _drop;
        }
        key = {
            hdr.ethernet.dstAddr: exact;
        }
        size = 512;
        default_action = _drop;
    }
    apply {
        forward_l2.apply();
    }
}

V1Switch(ParserImpl(), verifyChecksum(), ingress(), egress(), computeChecksum(), DeparserImpl()) main;
